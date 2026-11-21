---
id: R-OPS-032
level: 3
title: Automated tests on every supported platform
priority: should
status: accepted
links:
  refines: [F-OPS-006]
  constrains: [R-OPS-026, R-OPS-027, R-OPS-028]
---

# R-OPS-032 Automated tests on every supported platform

## Statement

The continuous integration shall run the platform-dependent checks (the Rust tests, building the program and a short start test of the built program) on every system and architecture of R-OPS-026 and R-OPS-042, and run the checks that are the same on every platform on Linux only.

## Acceptance criteria

- For every pull request, `cargo test` of the server, the release build of the program and a smoke test of the built program (start, serve the web client, upload, save a marking, backup, Ctrl+C) run on Linux x86_64, Linux arm64, Windows x86_64 and macOS arm64; macOS x86_64 runs the same but does not block (R-OPS-042).
- Submodule pinning, agent-docs check, UI-literals lint, rustfmt, clippy (host and wasm32), the documentation builds and the database check (R-OPS-038) run on Linux x86_64 only.
- The container image is built for linux/amd64 and linux/arm64 at least for every release (R-OPS-028).

## Notes

User decision: only what can differ between platforms runs everywhere, to keep CI time and cost low. Today CI (`.github/workflows/rust.yml`) runs only on Linux x86_64 and builds no image. GitHub offers hosted runners for Linux arm64, Windows and macOS (arm64 and x86_64).
