---
id: R-READ-016
level: 3
title: Librarians correct the systems
priority: should
status: verified
links:
  refines: [F-READ-003]
  depends_on: [R-READ-010]
  verified_by:
    - crates/musicus-server/tests/api.rs::librarians_correct_system_layouts_for_everyone
    - crates/musicus-server/src/layout/mod.rs::tests
    - crates/musicus-api/src/layout.rs::tests
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-server/src/routes/files.rs
    - crates/musicus-server/src/layout/mod.rs
    - crates/musicus-web/src/pages/layout_edit.rs
---

# R-READ-016 Librarians correct the systems

## Statement

A librarian shall be able to correct the detected layout of every page of a file version: move, add and delete cut lines (which merges and splits systems), mark a band as system, header or hidden, and mark a page to be shown whole; the correction shall apply to all members, override the automatic detection and survive a new detection run.

## Acceptance criteria

- After a correction, every member's system view of that file follows it.
- A correction can be reset to the automatic detection.
- Members cannot change layouts (403); a page that was not analysed yet cannot be corrected (409).
- A cut line can be moved by dragging or with the arrow keys; Split adds a cut, × removes one.
