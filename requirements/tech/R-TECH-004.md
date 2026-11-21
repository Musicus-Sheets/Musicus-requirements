---
id: R-TECH-004
level: 3
title: Database access in storage modules
priority: should
status: accepted
links:
  refines: [F-TECH-002]
  constrains: [R-ACL-001]
---

# R-TECH-004 Database access in storage modules

## Statement

All database access of the server shall go through storage modules, one per data area; request handlers shall contain no SQL.

## Acceptance criteria

- No SQL statement appears in `crates/musicus-server/src/routes/`; a check (test or script) fails otherwise.
- Every storage function that returns parts, pieces, files, programmes or annotations applies the access rule (R-ACL-001).

## Notes

Prepares a database replacement; does not change R-TECH-001 (embedded SQLite stays). SQL stays static (R-SEC-006).
