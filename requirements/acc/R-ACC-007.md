---
id: R-ACC-007
level: 3
title: Change password
priority: must
status: verified
links:
  refines: [F-ACC-002]
  verified_by: [crates/musicus-server/tests/api.rs::user_administration]
  implemented_by:
    - crates/musicus-server/src/routes/auth.rs
    - crates/musicus-web/src/pages/account.rs
---

# R-ACC-007 Change password

## Statement

When a user changes their password, the system shall require the current password and end all other sessions of that user.

## Acceptance criteria

- After the change, the current device stays logged in and another device is logged out.
