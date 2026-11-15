---
id: R-ACC-014
level: 3
title: Members see the same views without management options
priority: must
status: verified
links:
  refines: [F-ACC-004]
  depends_on: [R-ACC-009]
  verified_by:
    - e2e/smoke.mjs
    - crates/musicus-server/tests/api.rs::members_only_reach_granted_parts
    - crates/musicus-server/tests/api.rs::instruments_are_listed_for_everyone_and_kept_while_in_use
  implemented_by:
    - crates/musicus-web/src/ui.rs
    - crates/musicus-web/src/pages/library.rs
    - crates/musicus-web/src/pages/programmes.rs
    - crates/musicus-web/src/pages/instruments.rs
  decided_in: [tech:d-inline-management]
---

# R-ACC-014 Members see the same views without management options

## Statement

When a member is logged in, the web client shall show the library, programme and instrument views without any control to add, edit or delete, and the server shall keep refusing every management request of a member regardless of the user interface.

## Acceptance criteria

- A member's library has no "Add piece" and no "Edit" action; the programme list has no "New programme", a programme has no "Edit".
- A member's instrument list has no add form and no edit or delete buttons.
- A member's navigation has no Groups and no Users entry.
- A member creating a score or an instrument, or deleting an instrument, gets HTTP 403.
