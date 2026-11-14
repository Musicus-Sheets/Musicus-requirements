---
id: R-LIB-003
level: 3
title: Controlled instrument vocabulary
priority: must
status: implemented
links:
  refines: [F-LIB-001]
  implemented_by:
    - crates/musicus-server/src/routes/groups.rs
    - crates/musicus-server/migrations/0001_init.sql
---

# R-LIB-003 Controlled instrument vocabulary

## Statement

The system shall keep instruments as a list maintained by librarians, with unique names (ignoring letter case), and shall refuse to delete an instrument that parts still use.

## Acceptance criteria

- Creating 'trumpet' when 'Trumpet' exists fails with HTTP 409.
- Deleting an instrument used by a part fails with HTTP 409.

## Notes

Free-text instruments would let 'Trp.', 'Trumpet' and 'Trompete' drift apart and silently break instrument grants (F-ACL-001).
