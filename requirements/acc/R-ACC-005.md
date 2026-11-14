---
id: R-ACC-005
level: 3
title: Long-lived sessions
priority: must
status: implemented
links:
  refines: [F-ACC-002]
  implemented_by: [crates/musicus-server/src/auth.rs]
  decided_in: [tech:d-sessions]
---

# R-ACC-005 Long-lived sessions

## Statement

The system shall keep a session valid for a configurable number of days since its last use (default 60).

## Acceptance criteria

- A tablet used weekly stays logged in.
- A session unused for longer than the limit requires a new login.
