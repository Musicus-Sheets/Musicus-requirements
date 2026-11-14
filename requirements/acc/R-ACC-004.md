---
id: R-ACC-004
level: 3
title: Login
priority: must
status: verified
links:
  refines: [F-ACC-001]
  depends_on: [R-SEC-002]
  verified_by:
    - crates/musicus-server/tests/api.rs::login_sessions_and_csrf
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-server/src/routes/auth.rs
    - crates/musicus-server/src/auth.rs
  decided_in: [tech:d-hashing]
---

# R-ACC-004 Login

## Statement

The system shall log a user in with username (any letter case) and password, and shall answer wrong usernames and wrong passwords identically, also in response time.

## Acceptance criteria

- 'ADMIN' with the correct password logs in.
- Unknown user and wrong password both yield HTTP 401 with the same message.
