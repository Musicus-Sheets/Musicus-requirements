---
id: R-OPS-036
level: 3
title: Requirements and documentation tagged per release
priority: must
status: accepted
links:
  refines: [F-OPS-007]
---

# R-OPS-036 Requirements and documentation tagged per release

## Statement

For each release, the requirements repository and the documentation repositories (technical documentation and user guide) shall have a git tag with the release version on the commit that the release pins.

## Acceptance criteria

- For release tag `vX.Y.Z` of the main repository, the repositories `docs/requirements`, `docs/technical` and `docs/user-guide` each have tag `vX.Y.Z` on the commit of their submodule pointer in that release.

## Notes

A tag is enough; the requirements need no version on a title page. User decision: the maintainer creates the three tags by hand after the release pipeline (R-OPS-049) succeeded; no automation with tokens for the documentation repositories for now. The commands are in `RELEASING.md`.
