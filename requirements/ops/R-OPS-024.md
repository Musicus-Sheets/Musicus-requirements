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
    - .github/workflows/release.yml
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

A release build is one built with `MUSICUS_RELEASE_BUILD=1` (a-update-runner); every other build, including `cargo build --release` and local Docker images, is a development build. The release pipeline (R-OPS-049) builds every platform's program with the flag and starts it in its smoke test before anything is published, so a release build with previews fails stage 1 (the release check R-OPS-040 fails earlier on previews as well). `build.rs` also refuses a release build without the built-in web client (R-OPS-030).
