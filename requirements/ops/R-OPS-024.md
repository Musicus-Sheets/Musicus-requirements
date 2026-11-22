---
id: R-OPS-024
level: 3
title: Release builds contain no preview updates
priority: must
status: implemented
links:
  refines: [F-OPS-005]
  depends_on: [R-OPS-023]
  decided_in: [tech:d-update-model]
  implemented_by:
    - crates/musicus-server/src/updates/mod.rs
    - crates/musicus-server/build.rs
  verified_by:
    - crates/musicus-server/src/updates/mod.rs::release_builds_refuse_previews
    - crates/musicus-server/tests/updates.rs::previews_are_merged_and_recognised_by_the_release_update
---

# R-OPS-024 Release builds contain no preview updates

## Statement

A release build shall refuse to start if it contains preview database updates.

## Acceptance criteria

- A release build made from a tree with a file in the preview folder exits at start with a message naming the file; the release workflow fails before publishing.
- Development builds apply preview updates normally.

## Notes

A release build is one built with `MUSICUS_RELEASE_BUILD=1` (a-update-runner); every other build, including `cargo build --release` and local Docker images, is a development build. The release workflow that sets the flag and fails before publishing is not built yet (R-OPS-040).
