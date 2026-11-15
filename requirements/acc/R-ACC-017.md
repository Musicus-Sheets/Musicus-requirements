---
id: R-ACC-017
level: 3
title: Assignments of existing groups and parts are saved immediately
priority: should
status: verified
links:
  refines: [F-ACC-004]
  depends_on: [R-ACC-016, R-ACL-004]
  verified_by: [e2e/smoke.mjs]
  implemented_by:
    - crates/musicus-web/src/pages/groups.rs
    - crates/musicus-web/src/pages/forms.rs
---

# R-ACC-017 Assignments of existing groups and parts are saved immediately

## Statement

When the assignments of an existing group or an existing part change, by closing the dropdown with new entries or by removing an entry, the web client shall save the change at once, confirm it briefly with "Saved", and on failure show the error and restore the previous list.

## Acceptance criteria

- Group members (admins), instrument grants and score grants (librarians and admins) are stored without a Save button; a reload shows the new lists.
- Changing the instruments of an existing part stores only the instruments; the other fields keep their stored values until "Save part".
- In the guided flow for a new piece and in the programme editor the selection is part of the form and is saved with it.
- The server keeps checking every request: a librarian has no member controls, and the server refuses member changes by non-admins.
