---
id: R-OPS-022
level: 3
title: Restore command
priority: must
status: accepted
links:
  refines: [F-OPS-002]
  decided_in: [tech:d-update-model]
---

# R-OPS-022 Restore command

## Statement

The system shall provide a command that replaces the database of a stopped installation with a backup or snapshot and keeps the replaced database.

## Acceptance criteria

- `musicus-server restore --from <file>` with the server stopped makes the next start use that state.
- The replaced database is kept next to it under a new name; nothing in `blobs/` is changed.
- The command refuses while a server uses the data directory, and refuses a file that is not a Musicus database, in both cases without changing anything.
- Restoring a backup of an older release is allowed; the next start upgrades it (R-OPS-011).

## Notes

Replaces the manual procedure in the user guide (delete `-wal`/`-shm`, copy the file).
