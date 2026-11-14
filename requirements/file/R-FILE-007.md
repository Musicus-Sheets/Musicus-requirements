---
id: R-FILE-007
level: 3
title: Configurable client caching
priority: must
status: verified
links:
  refines: [F-FILE-002]
  conflicts_with:
    - id: R-PERF-007
      note: 'No-store means every reload downloads the sheets again; operators who accept browser caches can switch to ''immutable''.'
  verified_by: [crates/musicus-server/tests/api.rs::members_only_reach_granted_parts]
  implemented_by:
    - crates/musicus-server/src/routes/files.rs
    - crates/musicus-server/src/config.rs
  decided_in: [tech:d-no-client-storage]
---

# R-FILE-007 Configurable client caching

## Statement

The system shall by default forbid clients to store downloaded files (Cache-Control: private, no-store), and shall allow operators to permit private caching of files instead.

## Acceptance criteria

- Without configuration, file responses carry 'Cache-Control: private, no-store'.
- With MUSICUS_CLIENT_CACHE=immutable, they carry 'private, max-age=31536000, immutable'.
