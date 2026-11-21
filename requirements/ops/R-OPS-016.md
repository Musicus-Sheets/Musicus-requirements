---
id: R-OPS-016
level: 3
title: Data created only in the newer release on downgrade
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  decided_in: [tech:d-update-model]
---

# R-OPS-016 Data created only in the newer release on downgrade

## Statement

When an installation is taken back to an older release, data that only the newer release can represent shall be dropped, all other data shall stay, and after the next upgrade the newer release shall rebuild its own data from the data as the older release left it.

## Acceptance criteria

- Test: upgrade to N, create data that only N can store (for example a new kind of marking) and data that N−1 can store (a new annotation page); downgrade to N−1: the second is there; upgrade to N again: the second is still there, the first is gone and does not come back.
- Changes made with the older release (edited, added or deleted data) are visible after the next upgrade.
- After the next upgrade, derived data (search index, system layouts) matches the data, without a manual step.

## Notes

Accepted by the user as the price of a simple model: data that exists only in a newer release is not kept on the side while an older release runs.
