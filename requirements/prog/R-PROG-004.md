---
id: R-PROG-004
level: 3
title: Free memory of other programmes
priority: must
status: implemented
links:
  refines: [F-PROG-002]
  constrains: [R-PROG-003]
  implemented_by:
    - crates/musicus-web/src/pages/programmes.rs
    - crates/musicus-web/js/bridge.js
---

# R-PROG-004 Free memory of other programmes

## Statement

When a member opens a programme, the web client shall release the in-memory sheets of all other programmes.

## Acceptance criteria

- After switching programmes, only the sheets of the current programme remain in memory.
