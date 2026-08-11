#!/usr/bin/env python3
"""Migrate one deterministic shard of scan directories from GitHub to HF Xet."""

import argparse
import base64
import hashlib
import json
import os
import subprocess
import tempfile
import time
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import requests
from huggingface_hub import CommitOperationAdd, HfApi
from huggingface_hub.errors import HfHubHTTPError


def stable_shard(value: str, count: int) -> int:
    return int(hashlib.sha256(value.encode()).hexdigest()[:16], 16) % count


def git_blob_oid(path: str, revision: str) -> str:
    return subprocess.run(
        ["git", "rev-parse", f"{revision}:{path}"], check=True,
        stdout=subprocess.PIPE, text=True,
    ).stdout.strip()


def fetch_github_blob(session: requests.Session, repo: str, oid: str) -> bytes:
    response = session.get(f"https://api.github.com/repos/{repo}/git/blobs/{oid}", timeout=120)
    response.raise_for_status()
    payload = response.json()
    if payload.get("encoding") != "base64":
        raise RuntimeError(f"Unsupported GitHub encoding for {oid}")
    return base64.b64decode(payload["content"])


def retry_delay(error: HfHubHTTPError, default: int = 300) -> int:
    raw = error.response.headers.get("Retry-After", str(default)) if error.response is not None else str(default)
    try:
        return max(5, int(float(raw)) + 5)
    except ValueError:
        try:
            target = parsedate_to_datetime(raw)
            return max(5, int((target - datetime.now(timezone.utc)).total_seconds()) + 5)
        except (TypeError, ValueError):
            return default + 5


def retry_hf(label: str, call, *args, **kwargs):
    for attempt in range(30):
        try:
            return call(*args, **kwargs)
        except HfHubHTTPError as error:
            if error.response is None or error.response.status_code != 429 or attempt == 29:
                raise
            delay = retry_delay(error)
            print(json.dumps({"hf_operation": label, "rate_limited": True,
                              "retry_in_seconds": delay, "attempt": attempt + 1}), flush=True)
            time.sleep(delay)


def public_remote_sha1(repo_id: str, path: str) -> str:
    url = f"https://huggingface.co/datasets/{repo_id}/resolve/main/{quote(path)}"
    for attempt in range(30):
        response = requests.get(url, stream=True, timeout=180)
        if response.status_code != 429:
            response.raise_for_status()
            break
        delay = int(response.headers.get("Retry-After", "300")) + 5
        print(json.dumps({"hf_operation": "public_sample", "rate_limited": True,
                          "retry_in_seconds": delay, "attempt": attempt + 1}), flush=True)
        response.close()
        time.sleep(delay)
    else:
        raise RuntimeError(f"HF public sample remained rate-limited: {path}")
    digest = hashlib.sha1()
    for chunk in response.iter_content(1024 * 1024):
        digest.update(chunk)
    return digest.hexdigest()


def parse_manifest(path: Path) -> list[tuple[str, str]]:
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, relative = line.split(None, 1)
        entries.append((expected, relative))
    return entries


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard-index", type=int, required=True)
    parser.add_argument("--shard-count", type=int, required=True)
    parser.add_argument("--batch-size", type=int, default=50)
    parser.add_argument("--repo-id", default="Zual/TLG_libre_scans")
    parser.add_argument("--github-repo", default="l-pommeret/TLG_libre")
    parser.add_argument("--revision", default="HEAD")
    parser.add_argument("--local-blobs", action="store_true",
                        help="Materialize this shard through partial-clone Git transport instead of the REST blob API")
    args = parser.parse_args()
    if not 0 <= args.shard_index < args.shard_count:
        raise SystemExit("invalid shard index")

    api = HfApi(token=os.environ["HF_TOKEN"])
    known = set(retry_hf("list_repo_files", api.list_repo_files,
                         args.repo_id, repo_type="dataset"))
    manifests = sorted(Path("scans").glob("**/SHA1SUMS"))
    roots = [p.parent for p in manifests if stable_shard(p.parent.as_posix(), args.shard_count) == args.shard_index]
    if args.local_blobs:
        patterns = [
            "/scripts/migrate_all_scans_github_to_hf.py",
            "/scans/**/README.md",
            "/scans/**/SHA1SUMS",
            *(f"/{root}/**" for root in roots),
        ]
        subprocess.run(
            ["git", "sparse-checkout", "set", "--no-cone", "--stdin"],
            input="\n".join(patterns) + "\n", text=True, check=True,
        )
    github = requests.Session()
    github.headers.update({"Authorization": f"Bearer {os.environ['SOURCE_GITHUB_TOKEN']}", "Accept": "application/vnd.github+json"})

    migrated = skipped = commits = 0
    temporary_paths: list[Path] = []
    operations: list[CommitOperationAdd] = []
    expected_after_commit: list[tuple[str, str, int]] = []

    def flush() -> None:
        nonlocal commits, migrated, operations, temporary_paths, expected_after_commit, known
        if not operations:
            return
        try:
            retry_hf(
                "create_commit", api.create_commit,
                repo_id=args.repo_id, repo_type="dataset", operations=operations,
                commit_message=f"Migrate scan shard {args.shard_index + 1}/{args.shard_count}",
            )
            sizes = {}
            paths = [p for p, _, _ in expected_after_commit]
            for offset in range(0, len(paths), 100):
                info = retry_hf("get_paths_info", api.get_paths_info, args.repo_id,
                                paths=paths[offset:offset + 100], repo_type="dataset")
                sizes.update({item.path: item.size for item in info})
            for path, expected, size in expected_after_commit:
                if sizes.get(path) != size:
                    raise RuntimeError(f"HF size mismatch for {path}: {sizes.get(path)} != {size}")
                known.add(path)
            if expected_after_commit:
                sample_path, sample_sha1, _ = expected_after_commit[0]
                if public_remote_sha1(args.repo_id, sample_path) != sample_sha1:
                    raise RuntimeError(f"HF remote sample SHA-1 mismatch for {sample_path}")
            migrated += len(expected_after_commit)
            commits += 1
            print(json.dumps({"shard": args.shard_index, "commit": commits,
                              "uploaded": len(expected_after_commit),
                              "sample_sha1_verified": sample_path if expected_after_commit else None}), flush=True)
        finally:
            for temporary in temporary_paths:
                temporary.unlink(missing_ok=True)
            operations = []
            temporary_paths = []
            expected_after_commit = []

    for root in roots:
        for metadata in (root / "README.md", root / "SHA1SUMS"):
            remote_path = metadata.as_posix()
            if metadata.is_file() and remote_path not in known:
                operations.append(CommitOperationAdd(path_in_repo=remote_path, path_or_fileobj=remote_path))
                known.add(remote_path)
        for expected, relative in parse_manifest(root / "SHA1SUMS"):
            remote_path = f"{root}/{relative}"
            if remote_path in known:
                skipped += 1
                continue
            if args.local_blobs:
                content = Path(remote_path).read_bytes()
            else:
                oid = git_blob_oid(remote_path, args.revision)
                content = fetch_github_blob(github, args.github_repo, oid)
            actual = hashlib.sha1(content).hexdigest()
            if actual != expected:
                raise RuntimeError(f"GitHub SHA-1 mismatch for {remote_path}: {actual} != {expected}")
            with tempfile.NamedTemporaryFile(prefix="tlg-hf-", suffix=Path(relative).suffix, delete=False) as handle:
                handle.write(content)
                temporary = Path(handle.name)
            operations.append(CommitOperationAdd(path_in_repo=remote_path, path_or_fileobj=temporary.as_posix()))
            temporary_paths.append(temporary)
            expected_after_commit.append((remote_path, expected, len(content)))
            del content
            if len(expected_after_commit) >= args.batch_size:
                flush()
    flush()

    print(json.dumps({"shard": args.shard_index, "roots": len(roots), "migrated": migrated,
                      "skipped": skipped, "commits": commits, "temporary_images_retained": 0}), flush=True)


if __name__ == "__main__":
    main()
