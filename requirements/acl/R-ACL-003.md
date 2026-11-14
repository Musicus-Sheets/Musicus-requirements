---
id: R-ACL-003
level: 3
title: Changes apply immediately
priority: must
status: verified
links:
  refines: [F-ACL-001, F-ACL-002]
  verified_by: [crates/musicus-server/tests/api.rs::members_only_reach_granted_parts]
  implemented_by: [crates/musicus-server/src/access.rs]
  decided_in: [tech:d-access]
---

# R-ACL-003 Changes apply immediately

## Statement

The system shall apply changes to groups, memberships and grants to the next request of every affected user, without new login.

## Acceptance criteria

- Removing a member from 'Trumpets' makes their next library request return no trumpet parts.
