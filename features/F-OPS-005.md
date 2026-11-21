---
id: F-OPS-005
level: 2
title: Updates and downgrades
priority: must
status: accepted
links:
  refines: [G-005, G-006]
  depends_on: [F-OPS-002]
  decided_in: [tech:d-update-model]
---

# F-OPS-005 Updates and downgrades

## Statement

A volunteer administrator updates Musicus by replacing the program or the container image. Every newer release can be installed over any older one without losing data, and for a limited time a newer installation can be taken back to an older release by starting that release again.

## Rationale

Ensembles have no IT department (G-005): an update must not need knowledge of databases, and a failed or unwanted update must not cost the library or the members' markings (G-006). Being able to go back makes it safe to update shortly before a rehearsal.

## Notes

Guarantees start with release 1.0.0; there are no installations with real data before it. The downgrade window is R-OPS-014. Plan: docs/technical, chapter "Updates, downgrades and platforms" (label `updates`).
