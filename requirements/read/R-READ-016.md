---
id: R-READ-016
level: 3
title: Librarians correct the systems
priority: should
status: accepted
links:
  refines: [F-READ-003]
  depends_on: [R-READ-010]
---

# R-READ-016 Librarians correct the systems

## Statement

A librarian shall be able to correct the detected layout of every page of a file version: move, add and delete cut lines (which merges and splits systems), mark a band as system, header or hidden, and mark a page to be shown whole; the correction shall apply to all members, override the automatic detection and survive a new detection run.

## Acceptance criteria

- After a correction, every member's system view of that file follows it.
- A correction can be reset to the automatic detection.
- Members cannot change layouts (403).
