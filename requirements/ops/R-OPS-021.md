---
id: R-OPS-021
level: 3
title: Backup never changes the database
priority: must
status: accepted
links:
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

Today `backup` opens the database through the same function as `serve` and applies pending migrations first (`crates/musicus-server/src/main.rs`, `db.rs`).
