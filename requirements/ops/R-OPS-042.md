---
id: R-OPS-042
level: 3
title: Plain program on macOS with Intel processors
priority: should
status: accepted
links:
  refines: [F-OPS-006]
  depends_on: [R-OPS-026]
---

# R-OPS-042 Plain program on macOS with Intel processors

## Statement

The server should run as a plain program on macOS on Intel (x86_64) computers.

## Acceptance criteria

- CI builds the macOS x86_64 program and runs the smoke test (start, serve the web client, upload, save a marking, backup, Ctrl+C) on it.
- A failure on macOS x86_64 does not block a release; the release notes then say that this platform is not available.

## Notes

User decision: macOS on Apple silicon (arm64) is a must (R-OPS-026), macOS on Intel a should. Windows on ARM is not required.
