---
id: R-FILE-005
level: 3
title: Access check on every download
priority: must
status: verified
links:
  refines: [F-FILE-002]
  depends_on: [R-ACL-001, R-ACL-002]
  verified_by: [crates/musicus-server/tests/api.rs::members_only_reach_granted_parts]
  implemented_by: [crates/musicus-server/src/routes/files.rs]
---

# R-FILE-005 Access check on every download

## Statement

The system shall deliver a file or thumbnail only to users who may read at least one part using that file, and answer all other requests as if the file did not exist (HTTP 404).

## Acceptance criteria

- A trumpet player downloading the flute part's file by its hash gets HTTP 404.
- After removing the player from the group, the next download of the trumpet part fails with HTTP 404.
