---
id: R-OPS-045
level: 3
title: Reachable while starting
priority: must
status: verified
links:
  refines: [F-OPS-008]
  depends_on: [R-OPS-019]
  constrains: [R-OPS-007]
  decided_in: [tech:d-update-model]
  implemented_by:
    - crates/musicus-server/src/main.rs
    - crates/musicus-server/src/lifecycle.rs
    - crates/musicus-server/src/routes/mod.rs
    - crates/musicus-server/src/routes/events.rs
    - crates/musicus-server/src/error.rs
  verified_by:
    - crates/musicus-server/tests/lifecycle.rs::starting_answers_server_starting_until_ready
    - crates/musicus-server/tests/shutdown.rs::a_failed_start_ends_the_process_with_an_error
---

# R-OPS-045 Reachable while starting

## Statement

When the server starts, it shall listen at once and answer every request with a dedicated "starting" status until the snapshot, the database updates and the start-up checks are done; only the health check, the version, the event stream and the web client files answer meanwhile.

## Acceptance criteria

- During a start with database updates, `GET /api/health` and every other API request return HTTP 503 with error code `server_starting` and `Retry-After`, within one second of the process start; `GET /api/version` answers, `GET /api/events` sends `starting` and then `ready`.
- `GET /api/health` returns 200 `ok` only when the server is ready (R-OPS-007); "starting" counts as unhealthy.
- If the update fails (R-OPS-020) or the start fails otherwise, the server stops with a non-zero exit code; clients then see "Server not reachable".

## Notes

The listener opens before the database updates run, and the router answers `server_starting` until the state is ready. The Docker health check reports "starting" during `start-period` and "unhealthy" afterwards until the update is done (Docker does not restart the container for that); long updates on a Pi may need a longer `start-period`. New error code `server_starting` (a-error-codes). Event streams opened while starting are accepted without a session (there is no database to check one yet; they carry only the public phase and version).
