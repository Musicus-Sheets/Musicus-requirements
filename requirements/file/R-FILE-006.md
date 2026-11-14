---
id: R-FILE-006
level: 3
title: Conditional and partial downloads
priority: must
status: verified
links:
  refines: [F-FILE-002]
  verified_by: [crates/musicus-server/tests/api.rs::members_only_reach_granted_parts]
  implemented_by: [crates/musicus-server/src/routes/files.rs]
---

# R-FILE-006 Conditional and partial downloads

## Statement

The system shall mark every file with its hash as ETag, answer a matching If-None-Match with HTTP 304, and answer Range requests with the requested bytes (HTTP 206).

## Acceptance criteria

- A request with If-None-Match set to the file's ETag returns 304 without body.
- A request for bytes 0–7 returns 206 and '%PDF-1.7'.
