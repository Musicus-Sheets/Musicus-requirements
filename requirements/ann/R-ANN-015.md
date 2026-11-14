---
id: R-ANN-015
level: 3
title: Annotations follow access
priority: must
status: verified
links:
  refines: [F-ANN-004]
  depends_on: [R-ACL-001]
  verified_by:
    - crates/musicus-server/tests/api.rs::annotations_are_private_versioned_and_conflict_checked
  implemented_by: [crates/musicus-server/src/routes/annotations.rs]
---

# R-ANN-015 Annotations follow access

## Statement

When a member loses access to a part, the system shall hide the member's annotations on it without deleting them, and show them again if access is granted again.

## Acceptance criteria

- After removal from the group, loading the member's page returns HTTP 404; after re-adding, it loads again.
