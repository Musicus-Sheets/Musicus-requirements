---
id: R-ACC-006
level: 3
title: See and end sessions
priority: must
status: verified
links:
  refines: [F-ACC-002]
  verified_by:
    - crates/musicus-server/tests/api.rs::login_sessions_and_csrf
    - crates/musicus-server/tests/api.rs::user_administration
  implemented_by:
    - crates/musicus-server/src/routes/auth.rs
    - crates/musicus-web/src/pages/account.rs
---

# R-ACC-006 See and end sessions

## Statement

The system shall show users their active sessions (device, last use) and let them end any of them; logging out ends the current one.

## Acceptance criteria

- The account page lists 'this device' and other devices.
- After logging out, the old session cookie is rejected with HTTP 401.
