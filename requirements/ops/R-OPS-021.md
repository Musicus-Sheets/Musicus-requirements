---
id: R-OPS-021
level: 3
title: Backup never changes the database
priority: must
status: verified
links:
  verified_by:
    - crates/musicus-server/tests/snapshots.rs::backup_copies_a_newer_release_database_without_updating_it
    - crates/musicus-server/tests/snapshots.rs::backup_works_while_the_server_writes
  implemented_by:
    - crates/musicus-server/src/backup.rs
  refines: [F-OPS-002]
  constrains: [R-OPS-005]
  decided_in: [tech:d-update-model]
---

# R-OPS-021 Backup never changes the database

## Statement

The backup command shall copy the database as it is and shall never apply database updates.

## Acceptance criteria

- Running `backup` of a newer release on a data directory of an older release writes a copy of the older state; the database version marker is unchanged afterwards.
- `backup` works on a data directory that the running program could not start on (outside its window).

## Notes

`backup` opens the database read-only and never runs the update runner. It may leave empty `-wal`/`-shm` files next to the database of a stopped server (SQLite's read-only access to a WAL database); the database file itself is unchanged.
