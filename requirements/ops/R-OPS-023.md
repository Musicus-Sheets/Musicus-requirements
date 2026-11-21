---
id: R-OPS-023
level: 3
title: Preview database updates merged per release
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  decided_in: [tech:d-update-model]
---

# R-OPS-023 Preview database updates merged per release

## Statement

The release process shall merge all database updates made during development (preview updates) into one database update per release, such that a development database that has applied all of them accepts the release update without running it again.

## Acceptance criteria

- A developer's database that applied the preview updates of a branch keeps working after the branch is merged and after the release merges the previews.
- After a release, its database update is one file named after the release; its preview files are gone.
- A merged preview is never edited; a correction is a new preview.

## Notes

Details (file layout `migrations/preview/NNNN-<topic>.sql`, the list of contained previews in the release update, the merge script) are a design to be confirmed during implementation. Needs an own small migration runner instead of `sqlx::migrate!`, which refuses unknown or merged migrations. The existing migrations 0001–0010 are collapsed into one 1.0.0 baseline at the first release.
