---
id: R-READ-019
level: 3
title: System layouts of a programme ahead
priority: should
status: implemented
links:
  refines: [F-READ-003]
  depends_on: [R-PROG-003, R-READ-010]
  conflicts_with:
    - id: R-SEC-001
      note: Layouts are kept in memory only, like the sheets.
  implemented_by: [crates/musicus-web/src/pages/programmes.rs, crates/musicus-web/src/layouts.rs]
---

# R-READ-019 System layouts of a programme ahead

## Statement

When a member opens a programme, the web client shall also load the system layouts of all its sheets into memory, so that the system view works on stage without network.

## Acceptance criteria

- After opening a programme, switching pieces in the system view makes no layout request.
