---
id: R-ACC-013
level: 3
title: Management actions inside the regular views
priority: should
status: verified
links:
  refines: [F-ACC-004]
  depends_on: [R-ACC-009]
  verified_by: [e2e/smoke.mjs]
  implemented_by:
    - crates/musicus-web/src/ui.rs
    - crates/musicus-web/src/pages/library.rs
    - crates/musicus-web/src/pages/programmes.rs
    - crates/musicus-web/src/pages/instruments.rs
    - crates/musicus-web/src/pages/score_edit.rs
    - crates/musicus-web/src/pages/programme_edit.rs
  decided_in: [tech:d-inline-management]
---

# R-ACC-013 Management actions inside the regular views

## Statement

When a librarian or admin is logged in, the web client shall offer the management actions in the regular views: adding a piece and editing each piece and each part in the library, creating and editing programmes in the programme views, and adding, editing and deleting instruments in the instrument list; groups (librarians and admins) and users (admins) shall have their own navigation entries, and there shall be no separate management area.

## Acceptance criteria

- The navigation of an admin shows Library, Programmes, Instruments, Groups and Users, and no "Manage" entry; a librarian's navigation has no Users entry.
- A librarian adds a piece from the library with its details and its parts, each with a PDF, and returns to the library with the new piece highlighted.
- Every piece and every part in a librarian's library has an "Edit" action; the part's edit view uploads and replaces its PDF and lists its versions.
- A programme is created from the programme list and edited from the programme view.
- Deleting an instrument still used by parts shows the server's refusal (HTTP 409) as a message.
