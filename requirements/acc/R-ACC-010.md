---
id: R-ACC-010
level: 3
title: Password reset by new invite
priority: must
status: implemented
links:
  refines: [F-ACC-001]
  implemented_by:
    - crates/musicus-server/src/routes/users.rs
    - crates/musicus-web/src/pages/manage.rs
---

# R-ACC-010 Password reset by new invite

## Statement

When an admin requests a new invite for an enabled user, the system shall replace any previous invite of that user with a new one-time link.

## Acceptance criteria

- The new link works; the previous one no longer does.
