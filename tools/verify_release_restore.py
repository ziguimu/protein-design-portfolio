#!/usr/bin/env python3
"""Verify and optionally restore a release ZIP that contains MANIFEST.json."""
from __future__ import annotations
import argparse
import hashlib
import json
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath


def safe_member(name: str) -> PurePosixPath:
    p = PurePosixPath(name)
    if p.is_absolute() or not p.parts or any(part in ("", ".", "..") for part in p.parts):
        raise ValueError(f"unsafe archive path: {name!r}")
    return p


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("archive", type=Path, help="Release ZIP containing MANIFEST.json")
    ap.add_argument("--dest", type=Path, help="New empty directory for clean extraction")
    ap.add_argument("--report", type=Path, help="Write a JSON report here")
    args = ap.parse_args()
    report = {"archive": str(args.archive), "status": "FAIL", "files_expected": 0,
              "files_verified": 0, "source_byte_identical": 0, "transformed_files": 0,
              "missing": [], "size_mismatch": [], "sha256_mismatch": [],
              "unsafe_paths": [], "unexpected_members": [], "zip_crc_error": None}
    try:
        with zipfile.ZipFile(args.archive) as zf:
            names = [i.filename for i in zf.infolist()]
            if len(names) != len(set(names)):
                raise ValueError("archive contains duplicate member names")
            bad = zf.testzip()
            report["zip_crc_error"] = bad
            if bad:
                raise ValueError(f"ZIP CRC check failed for {bad}")
            manifest_member = next((n for n in names if n.lower() == "manifest.json"), None)
            if manifest_member is None:
                legacy = [n for n in names if PurePosixPath(n).name.startswith("archive_manifest_")
                          and PurePosixPath(n).suffix.lower() == ".json"]
                if len(legacy) != 1:
                    raise ValueError("MANIFEST.json or exactly one archive_manifest_*.json missing")
                manifest_member = legacy[0]
            manifest = json.loads(zf.read(manifest_member))
            files = manifest.get("files")
            if not isinstance(files, list):
                raise ValueError("manifest.files must be an array")
            # Earlier project ZIPs used bytes/sha256; current assets use
            # published_bytes/published_sha256 and may include redaction metadata.
            files = [dict(item,
                          published_bytes=item.get("published_bytes", item.get("bytes")),
                          published_sha256=item.get("published_sha256", item.get("sha256")),
                          source_sha256=item.get("source_sha256", item.get("sha256", "")))
                     for item in files]
            report["files_expected"] = len(files)
            member_map = {i.filename: i for i in zf.infolist()}
            expected_members = {manifest_member}
            root = args.dest.resolve() if args.dest else None
            if root:
                root.mkdir(parents=True, exist_ok=True)
                if any(root.iterdir()):
                    raise ValueError("--dest must be empty")
            for item in files:
                rel = safe_member(item["archive_path"])
                member = rel.as_posix()
                expected_members.add(member)
                info = member_map.get(member)
                if info is None:
                    report["missing"].append(member)
                    continue
                mode = info.external_attr >> 16
                if stat.S_ISLNK(mode):
                    report["unsafe_paths"].append(member)
                    continue
                h = hashlib.sha256()
                n = 0
                target = root.joinpath(*rel.parts) if root else None
                if target:
                    resolved = target.resolve()
                    try:
                        resolved.relative_to(root)
                    except ValueError:
                        report["unsafe_paths"].append(member)
                        continue
                    target.parent.mkdir(parents=True, exist_ok=True)
                    if target.exists():
                        raise ValueError(f"destination member already exists: {member}")
                    stream_out = target.open("xb")
                else:
                    stream_out = None
                try:
                    with zf.open(info) as stream_in:
                        while True:
                            b = stream_in.read(8 * 1024 * 1024)
                            if not b:
                                break
                            n += len(b)
                            h.update(b)
                            if stream_out:
                                stream_out.write(b)
                finally:
                    if stream_out:
                        stream_out.close()
                if n != int(item["published_bytes"]):
                    report["size_mismatch"].append({"path": member, "expected": int(item["published_bytes"]), "actual": n})
                elif h.hexdigest().lower() != item["published_sha256"].lower():
                    report["sha256_mismatch"].append({"path": member, "expected": item["published_sha256"], "actual": h.hexdigest()})
                else:
                    report["files_verified"] += 1
                    if item.get("source_sha256", "").lower() == item["published_sha256"].lower():
                        report["source_byte_identical"] += 1
                    else:
                        report["transformed_files"] += 1
            report["unexpected_members"] = sorted(set(names) - expected_members)
        good = (report["files_expected"] == report["files_verified"] and not report["missing"]
                and not report["size_mismatch"] and not report["sha256_mismatch"]
                and not report["unsafe_paths"] and not report["unexpected_members"])
        report["status"] = "PASS" if good else "FAIL"
    except Exception as e:
        report["error"] = f"{type(e).__name__}: {e}"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
