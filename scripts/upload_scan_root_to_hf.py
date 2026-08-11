#!/usr/bin/env python3
"""Upload one verified scan root to HF, then remove its transient images."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
from pathlib import Path

from huggingface_hub import CommitOperationAdd, HfApi

from migrate_scan_archives_to_hf import archive_name, pack_root


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("target_path")
    parser.add_argument("--repo-id", default="Zual/TLG_libre_scans")
    args = parser.parse_args()
    root = Path(args.target_path)
    if not root.as_posix().startswith("scans/") or ".." in root.parts:
        raise SystemExit("target_path must be a safe path below scans/")
    if not (root / "SHA1SUMS").is_file() or not (root / "images").is_dir():
        raise SystemExit("target root must contain SHA1SUMS and transient images/")

    fd, raw = tempfile.mkstemp(prefix="tlg-hf-root-", suffix=".tar")
    os.close(fd)
    temporary = Path(raw)
    remote = archive_name(root)
    try:
        digest, size, images = pack_root(root, temporary)
        api = HfApi(token=os.environ["HF_TOKEN"])
        api.create_commit(repo_id=args.repo_id, repo_type="dataset",
                          operations=[CommitOperationAdd(path_in_repo=remote,
                                                         path_or_fileobj=temporary.as_posix())],
                          commit_message=f"Store verified Greek scan root {root.as_posix()}")
        info = api.get_paths_info(args.repo_id, paths=[remote], repo_type="dataset")
        if len(info) != 1 or info[0].size != size:
            raise RuntimeError(f"remote size verification failed for {remote}")
        print(json.dumps({"archive": remote, "sha256": digest, "size": size,
                          "images": images, "remote_verified": True}), flush=True)
        shutil.rmtree(root / "images")
    finally:
        temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
