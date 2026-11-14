---
id: R-SEC-006
level: 3
title: No SQL injection
priority: must
status: implemented
links:
  refines: [F-SEC-002]
  implemented_by: [crates/musicus-server/src/routes]
  decided_in: [tech:d-static-sql]
---

# R-SEC-006 No SQL injection

## Statement

The system shall use only SQL statements fixed at compile time and pass all user input as bound parameters.

## Acceptance criteria

- The source contains no SQL built from user input.
