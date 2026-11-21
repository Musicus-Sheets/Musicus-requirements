---
id: R-OPS-032
level: 3
title: Automated tests on every supported platform
priority: should
status: proposed
links:
  refines: [F-OPS-006]
  constrains: [R-OPS-026, R-OPS-027, R-OPS-028]
---

# R-OPS-032 Automated tests on every supported platform

## Statement

The continuous integration shall build and test the server on every system and architecture of R-OPS-026 and build the container image for both architectures of R-OPS-028.

## Acceptance criteria

- `cargo test` of the server runs in CI on Linux x86_64, Linux arm64, Windows and macOS for every pull request.
- The image build for linux/amd64 and linux/arm64 runs at least for every release.

## Notes

Today CI (`.github/workflows/rust.yml`) runs only on Linux x86_64 and builds no image.
