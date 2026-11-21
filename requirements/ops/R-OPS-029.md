---
id: R-OPS-029
level: 3
title: Program files for every supported system
priority: should
status: proposed
links:
  refines: [F-OPS-006]
  depends_on: [R-OPS-026]
---

# R-OPS-029 Program files for every supported system

## Statement

Each release shall publish a ready-to-run program for every system and architecture of R-OPS-026, with checksums.

## Acceptance criteria

- The release page offers one download per system and architecture plus a checksum file.
- A downloaded program starts without installing Rust or other build tools.

## Notes

Proposed (follows from R-OPS-026 for volunteer administrators, not decided explicitly). macOS and Windows may warn about unsigned programs; signing is not planned.
