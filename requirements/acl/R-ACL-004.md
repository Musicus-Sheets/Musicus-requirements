---
id: R-ACL-004
level: 3
title: Managing groups and grants
priority: must
status: verified
links:
  refines: [F-ACL-001, F-ACL-002]
  depends_on: [R-ACC-009]
  verified_by: [e2e/smoke.mjs, crates/musicus-server/tests/api.rs::user_administration]
  implemented_by:
    - crates/musicus-server/src/routes/groups.rs
    - crates/musicus-web/src/pages/groups.rs
---

# R-ACL-004 Managing groups and grants

## Statement

The system shall let admins create, rename and delete groups and set their members, and let librarians set the instruments and scores granted to a group.

## Acceptance criteria

- The group page lists members, instruments and scores with checkboxes; saving replaces the lists.
