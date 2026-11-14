---
id: R-TECH-003
level: 3
title: Shared API types
priority: must
status: implemented
links:
  refines: [F-TECH-001]
  implemented_by: [crates/musicus-api]
  decided_in: [tech:d-shared-types]
---

# R-TECH-003 Shared API types

## Statement

Server and clients shall exchange data through a REST API whose request and response types are defined in one shared Rust crate.

## Acceptance criteria

- Changing a request type breaks the build of a client that was not updated.
