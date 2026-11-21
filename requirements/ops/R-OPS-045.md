---
id: R-OPS-045
level: 3
title: Reachable while starting
priority: must
status: accepted
links:
  refines: [F-OPS-008]
  depends_on: [R-OPS-019]
  constrains: [R-OPS-007]
  decided_in: [tech:d-update-model]
---

# R-OPS-045 Reachable while starting

## Statement

When the server starts, it shall listen at once and answer every request with a dedicated "starting" status until the snapshot, the database updates and the start-up checks are done.

## Acceptance criteria

- During a start with database updates, `GET /api/health` and every other API request return HTTP 503 with error code `server_starting` and `Retry-After`, within one second of the process start.
- `GET /api/health` returns 200 `ok` only when the server is ready (R-OPS-007).
- If the update fails (R-OPS-020), the server stops; clients then see "Server not reachable".

## Notes

Changes the start-up sequence: the listener opens before the database updates run, and the router answers `server_starting` until the state is ready. The Docker health check reports "starting/unhealthy" meanwhile; long updates on a Pi may need a longer `start-period`. New error code `server_starting` (a-error-codes).
