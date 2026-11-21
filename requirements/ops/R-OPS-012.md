---
id: R-OPS-012
level: 3
title: No data loss on upgrade
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  decided_in: [tech:d-update-model]
---

# R-OPS-012 No data loss on upgrade

## Statement

When the system upgrades a data directory, it shall keep all data, except data that belongs to a feature the release notes explicitly name as removed.

## Acceptance criteria

- Before and after the upgrade of a fixture data directory, the same users (with roles and passwords), groups, grants, instruments, pieces, parts, file versions, programmes, annotation sets with their pages, system layout corrections and import batches are returned by the API.
- Every stored file (blob) stays readable with the same SHA-256 hash.
- A release that removes a feature lists it, with the data concerned, in its release notes.

## Notes

Data the program can recompute (search index, detected system layouts) may be rebuilt instead of kept. Removed features: R-OPS-013.
