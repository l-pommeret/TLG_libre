#!/usr/bin/env python3
"""Stream one checked scan directory from GitHub into the HF binary store.

Image blobs are decoded into short-lived files under the system temporary
directory so hf_xet can upload them efficiently. They are deleted after every
upload. Authentication is read from the normal gh and Hugging Face credential
stores; no token is accepted on the command line or written by this script.
"""

import argparse
import base64
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import quote

import requests
from huggingface_hub import HfApi


def run(*args: str) -> bytes:
    return subprocess.run(args, check=True, stdout=subprocess.PIPE).stdout


def git_blob_sha(repo_path: str, revision: str) -> str:
    return run("git", "rev-parse", f"{revision}:{repo_path}").decode().strip()


def github_blob(repo: str, oid: str) -> bytes:
    payload = json.loads(run("gh", "api", f"repos/{repo}/git/blobs/{oid}"))
    if payload.get("encoding") != "base64":
        raise RuntimeError(f"Unsupported GitHub blob encoding for {oid}")
    return base64.b64decode(payload["content"])


def remote_sha1(repo_id: str, repo_path: str) -> tuple[str, int]:
    url = f"https://huggingface.co/datasets/{repo_id}/resolve/main/{quote(repo_path)}"
    response = requests.get(url, stream=True, timeout=120)
    response.raise_for_status()
    digest = hashlib.sha1()
    size = 0
    for chunk in response.iter_content(1024 * 1024):
        digest.update(chunk)
        size += len(chunk)
    return digest.hexdigest(), size


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_root", help="Tracked directory containing README.md, SHA1SUMS and images/")
    parser.add_argument("--repo-id", default="Zual/TLG_libre_scans")
    parser.add_argument("--github-repo", default="l-pommeret/TLG_libre")
    parser.add_argument("--revision", default="HEAD")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(args.source_root)
    sums = root / "SHA1SUMS"
    readme = root / "README.md"
    if not sums.is_file() or not readme.is_file():
        raise SystemExit("source_root must contain README.md and SHA1SUMS")

    entries = []
    for line in sums.read_text(encoding="utf-8").splitlines():
        expected, relative = line.split(None, 1)
        entries.append((expected, relative))
    print(json.dumps({"source_root": root.as_posix(), "images": len(entries), "dry_run": args.dry_run}))
    if args.dry_run:
        return

    api = HfApi()
    api.upload_file(path_or_fileobj=readme.as_posix(), path_in_repo=f"{root}/README.md", repo_id=args.repo_id, repo_type="dataset", commit_message=f"Add metadata for {root}")
    api.upload_file(path_or_fileobj=sums.as_posix(), path_in_repo=f"{root}/SHA1SUMS", repo_id=args.repo_id, repo_type="dataset", commit_message=f"Add checksums for {root}")

    completed = 0
    for expected, relative in entries:
        repo_path = f"{root}/{relative}"
        oid = git_blob_sha(repo_path, args.revision)
        content = github_blob(args.github_repo, oid)
        actual = hashlib.sha1(content).hexdigest()
        if actual != expected:
            raise RuntimeError(f"Source SHA-1 mismatch for {repo_path}: {actual} != {expected}")
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(prefix="tlg-hf-", suffix=Path(relative).suffix, delete=False) as handle:
                handle.write(content)
                temporary = Path(handle.name)
            del content
            api.upload_file(path_or_fileobj=temporary.as_posix(), path_in_repo=repo_path, repo_id=args.repo_id, repo_type="dataset", commit_message=f"Migrate {repo_path}")
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        hf_sha1, size = remote_sha1(args.repo_id, repo_path)
        if hf_sha1 != expected:
            raise RuntimeError(f"HF SHA-1 mismatch for {repo_path}: {hf_sha1} != {expected}")
        completed += 1
        print(json.dumps({"path": repo_path, "sha1": hf_sha1, "bytes": size, "verified": True}))
    print(json.dumps({"completed": completed, "temporary_images_retained": 0}))


if __name__ == "__main__":
    main()
