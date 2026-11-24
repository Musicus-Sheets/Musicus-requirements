---
id: R-OPS-043
level: 3
title: Orderly shutdown with a shutting-down answer
priority: must
status: verified
links:
  refines: [F-OPS-008]
  constrains: [R-OPS-008]
  decided_in: [tech:d-update-model]
  implemented_by:
    - crates/musicus-server/src/lifecycle.rs
    - crates/musicus-server/src/routes/mod.rs
    - crates/musicus-server/src/routes/events.rs
    - crates/musicus-server/src/main.rs
    - crates/musicus-server/src/db.rs
    - crates/musicus-server/src/config.rs
  verified_by:
    - crates/musicus-server/tests/lifecycle.rs::shutdown_announces_serves_the_grace_then_refuses_and_waits_for_running_requests
    - crates/musicus-server/tests/shutdown.rs::the_process_drains_and_exits_after_the_last_request
    - e2e/outage.mjs
---

# R-OPS-043 Orderly shutdown with a shutting-down answer

## Statement

When the server receives the stop signal, it shall announce "shutting down" to every open client at once, keep serving the requests that arrive during a short grace (so that clients can send what they have not saved yet), then answer every new request with a dedicated "shutting down" status, finish the requests still running, close the database cleanly and exit.

## Acceptance criteria

- After SIGTERM or Ctrl+C, every open event stream (`GET /api/events`) receives the state `shutting_down` at once.
- Requests that arrive during the grace (`MUSICUS_SHUTDOWN_GRACE_SECS`, default 3 s, at most 30 s; skipped when no event stream is open) are served normally, so the clients' last saves are stored.
- After the grace, a new request (for example saving an annotation page) is answered with HTTP 503, error code `server_shutting_down` and `Retry-After`, until the process exits; the change is not applied.
- Requests that were running before the grace ended (also an upload still sending its body) complete and are stored; the process waits at most 5 s for them.
- After the exit the database opens without a recovery step (WAL checkpointed, `-wal` empty or absent); the exit code is 0.
- With the default grace the process exits within the container's stop timeout (Docker default 10 s; `compose.yaml` 15 s) when no request hangs.

## Notes

Refines R-OPS-008 ("stop accepting connections and let running requests finish"): the listener stays open for the short drain so that clients get the dedicated answer instead of a broken connection. New error code `server_shutting_down` (a-error-codes). The clients block new actions first and then flush (R-OPS-044, R-OPS-047); the grace exists for that flush. Design: docs/agents decision a-client-outage.
