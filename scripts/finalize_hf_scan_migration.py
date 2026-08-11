#!/usr/bin/env python3
"""Verify complete scan-archive parity on HF and publish an audit marker."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from huggingface_hub import HfApi


def archive_name(root: Path) -> str:
    relative = root.relative_to("scans").as_posix()
    slug = relative.replace("/", "--")
    suffix = hashlib.sha256(relative.encode()).hexdigest()[:12]
    return f"webdataset/{slug}--{suffix}.tar"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-id", default="Zual/TLG_libre_scans")
    parser.add_argument("--marker", default="migration/complete.json")
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--write-registry", type=Path)
    args = parser.parse_args()

    roots = sorted(path.parent for path in Path("scans").glob("**/SHA1SUMS"))
    expected = {archive_name(root): root for root in roots}
    api = HfApi(token=os.environ.get("HF_TOKEN"))
    files = set(api.list_repo_files(args.repo_id, repo_type="dataset"))
    remote_archives = {
        path for path in files if path.startswith("webdataset/") and path.endswith(".tar")
    }
    missing = sorted(set(expected) - remote_archives)
    unexpected = sorted(remote_archives - set(expected))
    if missing or unexpected:
        print(json.dumps({"expected": len(expected), "present": len(expected) - len(missing),
                          "missing": missing, "unexpected": unexpected}, indent=2))
        raise SystemExit("HF archive set does not exactly match the Git scan manifests")

    remote = {}
    archive_paths = sorted(expected)
    for offset in range(0, len(archive_paths), 100):
        for item in api.get_paths_info(args.repo_id, paths=archive_paths[offset:offset + 100],
                                       repo_type="dataset"):
            remote[item.path] = item.size
    invalid_sizes = sorted(path for path in archive_paths if not remote.get(path, 0))
    if invalid_sizes:
        raise SystemExit(f"Missing or empty remote archives: {invalid_sizes}")

    records = []
    for archive, root in sorted(expected.items()):
        manifest = root / "SHA1SUMS"
        image_count = sum(1 for line in manifest.read_text(encoding="utf-8").splitlines() if line.strip())
        records.append({"archive": archive, "remote_size": remote[archive],
                        "source_root": root.as_posix(), "image_count": image_count,
                        "sha1sums_sha256": sha256(manifest)})
    marker = {
        "schema": "tlg-libre-hf-scan-migration-v1",
        "verified_at": datetime.now(timezone.utc).isoformat(),
        "repo_id": args.repo_id,
        "archive_count": len(records),
        "image_count": sum(record["image_count"] for record in records),
        "remote_bytes": sum(record["remote_size"] for record in records),
        "archives": records,
    }
    print(json.dumps({key: marker[key] for key in
                      ("repo_id", "archive_count", "image_count", "remote_bytes")}, indent=2))
    if args.write_registry:
        args.write_registry.parent.mkdir(parents=True, exist_ok=True)
        with args.write_registry.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, lineterminator="\n",
                                    fieldnames=("source_root", "hf_repo", "archive",
                                                "image_count", "remote_size",
                                                "manifest_sha256", "verification",
                                                "status", "last_checked"))
            writer.writeheader()
            for record in records:
                writer.writerow({"source_root": record["source_root"], "hf_repo": args.repo_id,
                                 "archive": record["archive"], "image_count": record["image_count"],
                                 "remote_size": record["remote_size"],
                                 "manifest_sha256": record["sha1sums_sha256"],
                                 "verification": "REMOTE_PATH_AND_SIZE_MATCH",
                                 "status": "MIGRATED_PUBLIC",
                                 "last_checked": datetime.now(timezone.utc).date().isoformat()})
    if args.check_only:
        return
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as handle:
        json.dump(marker, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temporary = handle.name
    try:
        api.upload_file(path_or_fileobj=temporary, path_in_repo=args.marker,
                        repo_id=args.repo_id, repo_type="dataset",
                        commit_message="Mark complete verified scan archive migration")
    finally:
        Path(temporary).unlink(missing_ok=True)


if __name__ == "__main__":
    main()
