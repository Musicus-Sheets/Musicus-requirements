---
id: R-FILE-009
level: 3
title: Removal of unused files
priority: could
status: proposed
links:
  refines: [F-OPS-002]
  conflicts_with:
    - id: R-FILE-004
      note: 'Files stay immutable; only unreferenced files are removed, and only after a grace period so that older backups stay consistent.'
---

# R-FILE-009 Removal of unused files

## Statement

The system shall offer operators a way to delete stored files that no part version and no annotation set references any more, after a grace period.

## Acceptance criteria

- Files referenced by a database backup taken before the grace period remain available.
