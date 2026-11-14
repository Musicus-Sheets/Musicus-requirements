---
id: R-ACC-009
level: 3
title: Rights of the roles
priority: must
status: verified
links:
  refines: [F-ACC-003]
  verified_by:
    - crates/musicus-server/tests/api.rs::members_only_reach_granted_parts
    - crates/musicus-server/tests/api.rs::user_administration
  implemented_by: [crates/musicus-server/src/auth.rs, crates/musicus-web/src/ui.rs]
---

# R-ACC-009 Rights of the roles

## Statement

The system shall allow members to read granted parts and annotate them; librarians additionally to manage scores, parts, files, programmes, instruments and grants; admins additionally to manage users, groups and group membership.

## Acceptance criteria

- A member creating a score gets HTTP 403.
- A librarian creating a group gets HTTP 403; listing groups works.
