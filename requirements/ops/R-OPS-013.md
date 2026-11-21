---
id: R-OPS-013
level: 3
title: Data of a removed feature comes back on downgrade
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  depends_on: [R-OPS-014]
  decided_in: [tech:d-update-model]
---

# R-OPS-013 Data of a removed feature comes back on downgrade

## Statement

When a release removes a feature, the system shall keep that feature's stored data unchanged for as long as an older release that has the feature can still be started (R-OPS-014), so that it is available again after a downgrade to such a release.

## Acceptance criteria

- Test: data of a feature removed in release N is created with release N−1; after an upgrade to N and a downgrade back to N−1 within the window, the data is shown again unchanged.
- The stored data of the removed feature is deleted only by the step that also ends the downgrade window for the releases that had the feature (the deferred removal part, see the plan).
