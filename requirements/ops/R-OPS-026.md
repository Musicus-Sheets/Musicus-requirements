---
id: R-OPS-026
level: 3
title: Plain program on Linux, Windows and macOS
priority: must
status: accepted
links:
  refines: [F-OPS-006]
  depends_on: [R-OPS-001]
---

# R-OPS-026 Plain program on Linux, Windows and macOS

## Statement

The server shall run as a plain program, without Docker, on Linux, Windows and macOS.

## Acceptance criteria

- On each of Linux (x86_64, arm64), Windows (x86_64) and macOS (arm64, Apple silicon) the release program starts, serves the web client, accepts an upload, saves a marking, makes a backup and shuts down cleanly with Ctrl+C.
- Every function described in the user guide is available on all three systems.

## Notes

Known blocker (not fixed yet): the blob store syncs the folder after a rename with `File::open(dir)?.sync_all()` (`crates/musicus-server/src/blobs.rs`), which fails on Windows, so every upload would fail there. SIGTERM handling is Unix-only, which is fine (Ctrl+C works everywhere). Windows on ARM is not required (if it works, fine). macOS on Intel is R-OPS-042 (should, not a release blocker).
