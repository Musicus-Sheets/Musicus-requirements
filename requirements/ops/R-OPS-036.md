---
id: R-OPS-036
level: 3
title: Requirements tagged per release
priority: must
status: accepted
links:
  refines: [F-OPS-007]
---

# R-OPS-036 Requirements tagged per release

## Statement

For each release, the requirements repository shall have a git tag with the release version on the commit that the release pins.

## Acceptance criteria

- For release tag `vX.Y.Z` of the main repository, the requirements repository has tag `vX.Y.Z` on the commit of its submodule pointer in that release.

## Notes

A tag is enough; the requirements need no version on a title page.
