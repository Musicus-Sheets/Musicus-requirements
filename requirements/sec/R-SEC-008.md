---
id: R-SEC-008
level: 3
title: No internal details in errors
priority: must
status: implemented
links:
  refines: [F-SEC-002]
  implemented_by: [crates/musicus-server/src/error.rs]
---

# R-SEC-008 No internal details in errors

## Statement

The system shall answer internal errors with a generic message and log the details only on the server.

## Acceptance criteria

- A database error returns HTTP 500 with 'internal error'; the log contains the cause.
