---
id: R-ACC-002
level: 3
title: Accept an invite
priority: must
status: verified
links:
  refines: [F-ACC-001]
  verified_by:
    - crates/musicus-server/tests/api.rs::login_sessions_and_csrf
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-server/src/routes/auth.rs
    - crates/musicus-web/src/pages/login.rs
---

# R-ACC-002 Accept an invite

## Statement

When a user opens a valid invite link and chooses a password of 8 to 256 characters, the system shall set the password, invalidate all invites and sessions of that user, and log the user in.

## Acceptance criteria

- After accepting, the same link answers 'expired' (HTTP 404).
- A 7-character password is rejected.
