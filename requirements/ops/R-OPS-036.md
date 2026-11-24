---
id: R-OPS-036
level: 3
title: Requirements and documentation tagged per release
priority: must
status: implemented
links:
  refines: [F-OPS-007]
  depends_on: [R-OPS-049]
  implemented_by: [.github/workflows/release.yml]
---

# R-OPS-036 Requirements and documentation tagged per release

## Statement

For each release, the requirements repository and the documentation repositories (technical documentation and user guide) shall have a git tag with the release version on the commit that the release pins.

## Acceptance criteria

- For release tag `vX.Y.Z` of the main repository, the repositories `docs/requirements`, `docs/technical` and `docs/user-guide` each have tag `vX.Y.Z` on the commit of their submodule pointer in that release.

## Notes

A tag is enough; the requirements need no version on a title page. User decision (2026-11-25, replacing the earlier "by hand"): the release pipeline (R-OPS-049) creates the three tags in its job `tag`, right after the main repository's tag, with the token of its own GitHub App (Musicus Release Builder, installed on all four repositories; a `v*` tag ruleset in each lets only this app create, move or delete release tags). Each tag lands on the commit the release's submodule pointer names; a tag on another commit stops the job. Verified only after the first real run on GitHub.
