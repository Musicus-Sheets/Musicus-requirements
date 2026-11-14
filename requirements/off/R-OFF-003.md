---
id: R-OFF-003
level: 3
title: Offline lease and revocation
priority: should
status: proposed
links:
  refines: [F-OFF-001]
  depends_on: [R-ACL-001]
---

# R-OFF-003 Offline lease and revocation

## Statement

The app shall delete local data it is no longer allowed to read at the next synchronisation, and discard its key when it has not synchronised for a configurable time (default 30 days).

## Acceptance criteria

- After removal from a group and a sync, the part is gone from the device.
