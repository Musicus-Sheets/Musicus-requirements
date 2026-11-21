---
id: R-OPS-024
level: 3
title: Release builds contain no preview updates
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  depends_on: [R-OPS-023]
  decided_in: [tech:d-update-model]
---

# R-OPS-024 Release builds contain no preview updates

## Statement

A release build shall refuse to start if it contains preview database updates.

## Acceptance criteria

- A release build made from a tree with a file in the preview folder exits at start with a message naming the file; the release workflow fails before publishing.
- Development builds apply preview updates normally.
