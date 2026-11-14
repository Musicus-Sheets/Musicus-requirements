---
id: R-ACC-008
level: 3
title: Disable users
priority: must
status: verified
links:
  refines: [F-ACC-003, F-ACC-002]
  verified_by: [crates/musicus-server/tests/api.rs::user_administration]
  implemented_by: [crates/musicus-server/src/routes/users.rs]
---

# R-ACC-008 Disable users

## Statement

When an admin disables a user, the system shall end all sessions and invites of that user and refuse further logins, while keeping the user's annotations; admins shall not be able to disable themselves or remove their own admin role.

## Acceptance criteria

- A disabled user's session is rejected immediately with HTTP 401.
- An admin disabling their own account gets HTTP 409.
