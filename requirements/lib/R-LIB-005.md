---
id: R-LIB-005
level: 3
title: Members see only their part of the library
priority: must
status: verified
links:
  refines: [F-LIB-001]
  depends_on: [R-ACL-001]
  verified_by:
    - crates/musicus-server/tests/api.rs::members_only_reach_granted_parts
    - crates/musicus-server/tests/api.rs::programmes_and_search
    - e2e/smoke.mjs
  implemented_by: [crates/musicus-server/src/routes/library.rs]
---

# R-LIB-005 Members see only their part of the library

## Statement

The system shall list for a member only scores with at least one part the member may read, and within them only those parts; librarians and admins see all scores and parts.

## Acceptance criteria

- A trumpet player sees the march with only the trumpet part, not the flute part.
- A score without any readable part does not appear for the member, also not in search results.
