---
id: R-OPS-007
level: 3
title: Health check
priority: must
status: verified
links:
  refines: [F-OPS-003]
  verified_by: [crates/musicus-server/tests/api.rs::login_sessions_and_csrf]
  implemented_by:
    - crates/musicus-server/src/routes/mod.rs
    - crates/musicus-server/src/main.rs
  decided_in: [tech:d-distroless]
---

# R-OPS-007 Health check

## Statement

The system shall answer GET /api/health without login with 'ok' when it can read its database, and provide a 'healthcheck' command that exits with 0 only in that case.

## Acceptance criteria

- GET /api/health returns 200 'ok'.
- 'musicus-server healthcheck' exits with 1 when no server runs.
