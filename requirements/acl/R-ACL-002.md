---
id: R-ACL-002
level: 3
title: Denied as not found
priority: must
status: verified
links:
  refines: [F-ACL-001, F-SEC-002]
  verified_by: [crates/musicus-server/tests/api.rs::members_only_reach_granted_parts]
  implemented_by: [crates/musicus-server/src/access.rs]
  decided_in: [tech:d-access]
---

# R-ACL-002 Denied as not found

## Statement

The system shall answer requests for parts, files, programmes and annotations the user may not read exactly like requests for things that do not exist (HTTP 404).

## Acceptance criteria

- Requesting the flute part's versions as trumpet player returns HTTP 404, not 403.
