#!/usr/bin/env python3
"""Hash-guarded, exact-file cleanup helper. Dry-run unless --apply is supplied."""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import os
import sys
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def pid_alive(pid: int) -> bool:
    if os.name == "nt":
        # Native Windows PIDs cannot be checked reliably with ``os.kill(pid, 0)``
        # on every Python build. Query the process handle directly instead.
        import ctypes

        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        open_process = kernel32.OpenProcess
        open_process.argtypes = (ctypes.c_uint32, ctypes.c_int, ctypes.c_uint32)
        open_process.restype = ctypes.c_void_p
        close_handle = kernel32.CloseHandle
        close_handle.argtypes = (ctypes.c_void_p,)
        close_handle.restype = ctypes.c_int
        handle = open_process(0x1000, 0, pid)  # PROCESS_QUERY_LIMITED_INFORMATION
        if handle:
            close_handle(handle)
            return True
        return ctypes.get_last_error() == 5  # ERROR_ACCESS_DENIED means it exists.
    try:
        os.kill(pid, 0)
        return True
    except PermissionError:
        return True
    except (ProcessLookupError, OSError):
        return False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manifest", type=Path, help="CSV with source_path, sha256, cleanup_authorized")
    ap.add_argument("--root", required=True, type=Path, help="The only allowed deletion root")
    ap.add_argument("--active-path", action="append", default=[], help="File path currently used by an active task (repeatable)")
    ap.add_argument("--active-pid", action="append", type=int, default=[], help="If any listed PID is alive, skip every candidate")
    ap.add_argument("--apply", action="store_true", help="Delete only entries reported ready; default is dry-run")
    ap.add_argument("--report", type=Path, help="Write a JSON report here")
    args = ap.parse_args()
    root = args.root.resolve(strict=True)
    active_pids = [pid for pid in args.active_pid if pid_alive(pid)]
    active_paths = set()
    for raw in args.active_path:
        p = Path(raw)
        if not p.is_absolute():
            p = root / p
        active_paths.add(str(p.resolve(strict=False)).casefold())
    result = {"root": str(root), "mode": "apply" if args.apply else "dry_run", "active_pids_alive": active_pids,
              "ready": [], "deleted": [], "skipped": []}
    with args.manifest.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        raw = row.get("source_path", "")
        expected = row.get("sha256", "").strip().lower()
        if str(row.get("cleanup_authorized", "")).strip().lower() not in ("1", "true", "yes"):
            result["skipped"].append({"path": raw, "reason": "not_authorized_in_manifest"})
            continue
        if len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
            result["skipped"].append({"path": raw, "reason": "invalid_expected_sha256"})
            continue
        p = Path(raw)
        if not p.is_absolute():
            p = root / p
        resolved = p.resolve(strict=False)
        try:
            resolved.relative_to(root)
        except ValueError:
            result["skipped"].append({"path": raw, "reason": "outside_allowed_root"})
            continue
        if active_pids:
            result["skipped"].append({"path": raw, "reason": "active_pid_present"})
            continue
        if str(resolved).casefold() in active_paths:
            result["skipped"].append({"path": raw, "reason": "active_path"})
            continue
        if p.is_symlink() or any(parent.is_symlink() for parent in [p.parent, *p.parents] if parent != root.parent):
            result["skipped"].append({"path": raw, "reason": "symlink_path"})
            continue
        if not p.is_file():
            result["skipped"].append({"path": raw, "reason": "missing_or_not_a_file"})
            continue
        actual = sha256(p)
        if actual != expected:
            result["skipped"].append({"path": raw, "reason": "sha256_changed", "expected": expected, "actual": actual})
            continue
        if args.apply:
            p.unlink()
            result["deleted"].append({"path": raw, "sha256": actual})
        else:
            result["ready"].append({"path": raw, "sha256": actual})
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
