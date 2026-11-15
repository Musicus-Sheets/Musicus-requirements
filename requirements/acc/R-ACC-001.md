---
id: R-ACC-001
level: 3
title: Create accounts with an invite link
priority: must
status: verified
links:
  refines: [F-ACC-001]
  verified_by: [crates/musicus-server/tests/api.rs::user_administration, e2e/smoke.mjs]
  implemented_by:
    - crates/musicus-server/src/routes/users.rs
    - crates/musicus-web/src/pages/users.rs
  decided_in: [tech:d-invites]
---

# R-ACC-001 Create accounts with an invite link

## Statement

When an admin creates a user (username, display name, role), the system shall create the account without password and return a one-time invite link valid for 7 days.

## Acceptance criteria

- Creating 'Carla' returns an invite and the username 'carla'; the user list shows her as 'Invited'.
- Creating a second user 'carla' fails with HTTP 409.
- Usernames may contain only letters, digits, '.', '_' and '-'.
