---
id: R-OPS-028
level: 3
title: Container images for amd64 and arm64
priority: must
status: accepted
links:
  refines: [F-OPS-006]
---

# R-OPS-028 Container images for amd64 and arm64

## Statement

Each release shall publish one container image for linux/amd64 and linux/arm64 under its version tag.

## Acceptance criteria

- `docker pull <image>:<version>` gets a working image on an x86_64 PC and on a 64-bit Raspberry Pi.
- Each release has the tags `<major>.<minor>.<patch>` and `<major>.<minor>`; the Compose file of the release uses a version tag.

## Notes

Docker Desktop on Windows and macOS uses the same Linux images. Today images are built locally for the host only. Registry (for example GitHub Container Registry) to be decided at implementation.
