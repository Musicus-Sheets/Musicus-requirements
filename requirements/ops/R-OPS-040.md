---
id: R-OPS-040
level: 3
title: Release check
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  depends_on: [R-OPS-023, R-OPS-038]
  constrains: [R-OPS-018, R-OPS-024]
  decided_in: [tech:d-update-model]
---

# R-OPS-040 Release check

## Statement

On a release branch `release/<version>`, the continuous integration shall fail if the release's database updates do not match its version: a patch release may contain no database change, and a minor or major release may only replace all previews by one merged update for its version.

## Acceptance criteria

- Release pull requests are recognised by the branch name `release/<version>` (for example `release/1.3.0`); only they may delete preview updates and add `migrations/<version>.sql`.
- For a patch version (`x.y.Z`, Z > 0) the check fails if any preview update or a database update for this version exists.
- For a minor or major version the check fails if the merged update does not list exactly the preview updates that the pull request removes, or if a preview update remains.

## Notes

Enforces R-OPS-018 and R-OPS-024 before a release is published. Implemented with phase 0. Other release checks (version on the title pages, requirements tag) belong to the same workflow.
