---
id: R-OPS-043
level: 3
title: Orderly shutdown with a shutting-down answer
priority: must
status: accepted
links:
  refines: [F-OPS-008]
  constrains: [R-OPS-008]
  decided_in: [tech:d-update-model]
---

# R-OPS-043 Orderly shutdown with a shutting-down answer

## Statement

When the server receives the stop signal, it shall accept no further changes and answer every request that needs it with a dedicated "shutting down" status, finish the writes already in progress, close the database cleanly and then exit.

## Acceptance criteria

- After SIGTERM or Ctrl+C, a new change (for example saving an annotation page) is answered with HTTP 503, error code `server_shutting_down` and `Retry-After`, until the process exits; the change is not applied.
- Writes that started before the signal complete and are stored; after the exit the database opens without a recovery step (WAL checkpointed, `-wal` empty or absent).
- The process exits within the container's stop timeout (default 10 s in Docker) when no write hangs.

## Notes

Refines R-OPS-008 ("stop accepting connections and let running requests finish"): the listener stays open for the short drain so that clients get the dedicated answer instead of a broken connection. New error code `server_shutting_down` (a-error-codes).
