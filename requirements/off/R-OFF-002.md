---
id: R-OFF-002
level: 3
title: Synchronisation
priority: should
status: proposed
links:
  refines: [F-OFF-001]
  depends_on: [R-FILE-004, R-ANN-012]
---

# R-OFF-002 Synchronisation

## Statement

The app shall synchronise sheets by file hash and annotations by page revision, transferring only what changed.

## Acceptance criteria

- A second sync without changes transfers no file contents.
