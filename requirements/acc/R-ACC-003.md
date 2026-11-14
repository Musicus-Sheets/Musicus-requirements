---
id: R-ACC-003
level: 3
title: First administrator
priority: must
status: verified
links:
  refines: [F-ACC-001]
  verified_by: [crates/musicus-server/tests/api.rs]
  implemented_by: [crates/musicus-server/src/lib.rs, crates/musicus-server/src/main.rs]
  decided_in: [tech:d-invites]
---

# R-ACC-003 First administrator

## Statement

When the server starts with no users, it shall create the user 'admin' without password and write a one-time invite link for it to the log.

## Acceptance criteria

- A fresh installation logs a link /invite/<token>; no default password exists.
- A second start does not create another admin.
