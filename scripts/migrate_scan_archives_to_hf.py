#!/usr/bin/env python3
"""Pack deterministic scan-source roots and upload one HF commit per shard."""

import argparse
import csv
import hashlib
import json
import os
import subprocess
import tarfile
import tempfile
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

from huggingface_hub import CommitOperationAdd, HfApi
from huggingface_hub.errors import HfHubHTTPError


def stable_shard(value: str, count: int) -> int:
    return int(hashlib.sha256(value.encode()).hexdigest()[:16], 16) % count


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
    for attempt in range(40):
        try:
            return call(*args, **kwargs)
        except HfHubHTTPError as error:
            if error.response is None or error.response.status_code != 429 or attempt == 39:
                raise
            delay = retry_delay(error)
            print(json.dumps({"hf_operation": label, "rate_limited": True,
                              "retry_in_seconds": delay, "attempt": attempt + 1}), flush=True)
            time.sleep(delay)


def parse_manifest(path: Path) -> list[tuple[str, str]]:
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            expected, relative = line.split(None, 1)
            entries.append((expected, relative))
    return entries


def archive_name(root: Path) -> str:
    relative = root.relative_to("scans").as_posix()
    slug = relative.replace("/", "--")
    suffix = hashlib.sha256(relative.encode()).hexdigest()[:12]
    return f"webdataset/{slug}--{suffix}.tar"


def add_deterministic(tar: tarfile.TarFile, path: Path, arcname: str) -> None:
    info = tar.gettarinfo(path.as_posix(), arcname=arcname)
    info.uid = info.gid = 0
    info.uname = info.gname = ""
    info.mtime = 0
    with path.open("rb") as handle:
        tar.addfile(info, handle)


def pack_root(root: Path, destination: Path) -> tuple[str, int, int]:
    entries = parse_manifest(root / "SHA1SUMS")
    # Some narrowly targeted scan roots intentionally have no per-root README.
    # SHA1SUMS is authoritative; include README only when the root provides one.
    included = [root / "SHA1SUMS"]
    if (root / "README.md").is_file():
        included.insert(0, root / "README.md")
    included.extend(root / relative for _, relative in entries)
    expected_by_path = {relative: expected for expected, relative in entries}
    digest = hashlib.sha256()
    with tarfile.open(destination, mode="w", format=tarfile.PAX_FORMAT) as tar:
        for path in included:
            if not path.is_file():
                raise RuntimeError(f"Missing source file: {path}")
            relative = path.relative_to(root).as_posix()
            if relative in expected_by_path:
                image_digest = hashlib.sha1()
                with path.open("rb") as image:
                    for block in iter(lambda: image.read(8 * 1024 * 1024), b""):
                        image_digest.update(block)
                actual = image_digest.hexdigest()
                if actual != expected_by_path[relative]:
                    raise RuntimeError(f"SHA-1 mismatch: {path}: {actual} != {expected_by_path[relative]}")
            add_deterministic(tar, path, f"{root.as_posix()}/{relative}")
    with destination.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest(), destination.stat().st_size, len(entries)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard-index", type=int, required=True)
    parser.add_argument("--shard-count", type=int, required=True)
    parser.add_argument("--repo-id", default="Zual/TLG_libre_scans")
    parser.add_argument("--plan-only", action="store_true")
    args = parser.parse_args()
    if not 0 <= args.shard_index < args.shard_count:
        raise SystemExit("invalid shard index")

    manifests = sorted(Path("scans").glob("**/SHA1SUMS"))
    roots = [p.parent for p in manifests if stable_shard(p.parent.as_posix(), args.shard_count) == args.shard_index]
    print(json.dumps({"shard": args.shard_index, "roots": len(roots),
                      "archives": [archive_name(root) for root in roots]}), flush=True)
    if args.plan_only:
        return

    patterns = [
        "/scripts/migrate_scan_archives_to_hf.py",
        "/scans/**/README.md",
        "/scans/**/SHA1SUMS",
        *(f"/{root}/**" for root in roots),
    ]
    subprocess.run(["git", "sparse-checkout", "set", "--no-cone", "--stdin"],
                   input="\n".join(patterns) + "\n", text=True, check=True)

    api = HfApi(token=os.environ["HF_TOKEN"])
    known = set(retry_hf("list_repo_files", api.list_repo_files, args.repo_id, repo_type="dataset"))
    operations = []
    records = []
    temporary_paths = []
    try:
        for root in roots:
            remote = archive_name(root)
            if remote in known:
                records.append({"source_root": root.as_posix(), "archive": remote, "status": "already_present"})
                continue
            fd, raw = tempfile.mkstemp(prefix=f"tlg-wds-{args.shard_index}-", suffix=".tar")
            os.close(fd)
            temporary = Path(raw); temporary_paths.append(temporary)
            sha256, size, images = pack_root(root, temporary)
            operations.append(CommitOperationAdd(path_in_repo=remote, path_or_fileobj=temporary.as_posix()))
            records.append({"source_root": root.as_posix(), "archive": remote, "sha256": sha256,
                            "size": size, "images": images, "status": "uploaded"})
        if operations:
            retry_hf("create_archive_commit", api.create_commit, repo_id=args.repo_id,
                     repo_type="dataset", operations=operations,
                     commit_message=f"Add scan WebDataset archives shard {args.shard_index + 1}/{args.shard_count}")
        uploaded = [r for r in records if r["status"] == "uploaded"]
        for offset in range(0, len(uploaded), 100):
            group = uploaded[offset:offset + 100]
            info = retry_hf("verify_archive_sizes", api.get_paths_info, args.repo_id,
                            paths=[r["archive"] for r in group], repo_type="dataset")
            sizes = {item.path: item.size for item in info}
            for record in group:
                if sizes.get(record["archive"]) != record["size"]:
                    raise RuntimeError(f"Remote size mismatch: {record['archive']}")
        print(json.dumps({"shard": args.shard_index, "records": records,
                          "temporary_archives_retained": 0}), flush=True)
    finally:
        for path in temporary_paths:
            path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
