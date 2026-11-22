---
id: R-OPS-022
level: 3
title: Restore command
priority: must
status: verified
links:
  verified_by:
    - crates/musicus-server/tests/snapshots.rs::restore_replaces_the_database_and_keeps_the_old_one
  implemented_by:
    - crates/musicus-server/src/backup.rs
    - crates/musicus-server/src/main.rs
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

Replaced the manual procedure of the user guide (delete `-wal`/`-shm`, copy the file). A running server is detected by an operating-system lock on `musicus.lock` in the data directory, held by `serve` and `create-admin`; servers of releases before this command hold none. The replaced database is kept as `snapshots/replaced-<time>.sqlite`.
