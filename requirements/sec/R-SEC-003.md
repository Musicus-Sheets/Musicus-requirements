---
id: R-SEC-003
level: 3
title: Limit password guessing
priority: must
status: verified
links:
  refines: [F-SEC-002]
  verified_by:
    - crates/musicus-server/tests/api.rs::login_sessions_and_csrf
    - crates/musicus-server/src/auth.rs::limiter_blocks_after_ten_failures
  implemented_by:
    - crates/musicus-server/src/auth.rs
    - crates/musicus-server/src/routes/auth.rs
---

# R-SEC-003 Limit password guessing

## Statement

The system shall refuse login attempts with HTTP 429 after 10 failed attempts within 15 minutes for the same username or the same client address.

## Acceptance criteria

- The 11th wrong attempt within 15 minutes returns 429.
