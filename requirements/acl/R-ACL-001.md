---
id: R-ACL-001
level: 3
title: Read rule
priority: must
status: verified
links:
  refines: [F-ACL-001, F-ACL-002]
  verified_by: [crates/musicus-server/tests/api.rs::members_only_reach_granted_parts]
  implemented_by: [crates/musicus-server/src/access.rs]
  decided_in: [tech:d-access]
---

# R-ACL-001 Read rule

## Statement

The system shall let a user read a part if the user is a librarian or admin, or a member of a group that is granted one of the part's instruments, or a member of a group that is granted the part's score.

## Acceptance criteria

- Group 'Trumpets' with instrument 'Trumpet' reads every part tagged 'Trumpet'.
- Granting the score to 'Trumpets' additionally opens the flute part of that score.
