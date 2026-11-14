---
id: R-OPS-009
level: 3
title: Continuous database replication
priority: could
status: proposed
links:
  refines: [F-OPS-002]
---

# R-OPS-009 Continuous database replication

## Statement

The system shall support continuous replication of the database to another location (e.g. with Litestream), so that it can be restored to a recent point in time.

## Acceptance criteria

- After losing the server, the database can be restored to within a minute of the failure.

## Notes

Mitigates the single-node risk (no high availability); the blob directory is backed up separately (immutable files).
