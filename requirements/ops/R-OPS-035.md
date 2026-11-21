---
id: R-OPS-035
level: 3
title: Version on the documentation
priority: must
status: accepted
links:
  refines: [F-OPS-007]
---

# R-OPS-035 Version on the documentation

## Statement

The user guide and the technical documentation of a release shall name that release's version on their title page, and the user guide site shall name it on every page.

## Acceptance criteria

- The title page of the user guide PDF and of the technical documentation PDF, and the head of their HTML pages, show the release version (for example "Musicus 1.2").
- Every page of the user guide site shows the version it belongs to.
- The release check fails if the version on a title page differs from the release version.

## Notes

Partly in place: both title pages show a hand-written "0.1", and the guide site's version bar shows the release tag (docs/agents a-guide-site).
