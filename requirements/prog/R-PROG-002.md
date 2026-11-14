---
id: R-PROG-002
level: 3
title: Members see their programmes
priority: must
status: verified
links:
  refines: [F-PROG-001]
  depends_on: [R-ACL-001]
  verified_by: [crates/musicus-server/tests/api.rs::programmes_and_search]
  implemented_by: [crates/musicus-server/src/routes/programmes.rs]
---

# R-PROG-002 Members see their programmes

## Statement

The system shall show a member only programmes that contain at least one piece the member has a readable part for, and within them only those pieces with only those parts.

## Acceptance criteria

- A trumpet player sees the programme with the march twice and without the flute concerto.
- A programme without any readable piece is not listed for the member.
