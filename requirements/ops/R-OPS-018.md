---
id: R-OPS-018
level: 3
title: Patch releases contain no database changes
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  decided_in: [tech:d-update-model]
---

# R-OPS-018 Patch releases contain no database changes

## Statement

A patch release (X.Y.Z with Z > 0) shall contain no database update.

## Acceptance criteria

- The release check fails when a release whose patch number is not 0 contains a database update file that the previous release of the same minor did not contain.
- Any two releases of the same minor start on each other's data directories.

## Notes

Old minors get no new patches; fixes go into the next release (user decision). This is what makes R-OPS-014 (c) hold without any mechanism.
