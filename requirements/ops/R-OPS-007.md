---
id: R-OPS-007
level: 3
title: Health check
priority: must
status: verified
links:
  refines: [F-OPS-003]
  verified_by:
    - crates/musicus-server/tests/api.rs::login_sessions_and_csrf
    - crates/musicus-server/tests/lifecycle.rs::starting_answers_server_starting_until_ready
  implemented_by:
    - crates/musicus-server/src/routes/mod.rs
    - crates/musicus-server/src/main.rs
    - crates/musicus-server/src/listen.rs
    - crates/musicus-server/src/lifecycle.rs
  decided_in: [tech:d-distroless]
---

# R-OPS-007 Health check

## Statement

The system shall answer GET /api/health without login with 'ok' when it is ready and can read its database (503 while it starts or shuts down, R-OPS-045, R-OPS-043), and provide a 'healthcheck' command that exits with 0 only in that case.

## Acceptance criteria

- GET /api/health returns 200 'ok' when ready; 503 `server_starting` during the start, 503 `server_shutting_down` from the stop signal on.
- 'musicus-server healthcheck' exits with 1 when no server runs.
