---
id: R-OPS-023
level: 3
title: Preview database updates merged per release
priority: must
status: implemented
links:
  refines: [F-OPS-005]
  decided_in: [tech:d-update-model]
  implemented_by:
    - crates/musicus-server/src/updates/runner.rs
    - crates/musicus-server/src/updates/file.rs
    - crates/musicus-server/build.rs
    - scripts/release-migrations.py
  verified_by:
    - crates/musicus-server/tests/updates.rs::previews_are_merged_and_recognised_by_the_release_update
    - crates/musicus-server/tests/updates.rs::release_script_refuses_mistakes
---

# R-OPS-023 Preview database updates merged per release

## Statement

The release process shall merge all database updates made during development (preview updates) into one database update per release, such that a development database that has applied all of them accepts the release update without running it again.

## Acceptance criteria

- A developer's database that applied the preview updates of a branch keeps working after the branch is merged and after the release merges the previews.
- After a release, its database update is one file named after the release; its preview files are gone.
- A merged preview is never edited; a correction is a new preview.

## Notes

Implemented (a-update-runner): previews `crates/musicus-server/migrations/preview/NNNN-<topic>.sql`, the header line `-- @previews:` in the merged `migrations/X.Y.0.sql`, `scripts/release-migrations.py`. Preview removal parts never run on development databases; they run with the merged release update. The development migrations 0001–0010 became the baseline `migrations/1.0.0.sql`; databases that applied them are recognised once. Not yet checked automatically: "a merged preview is never edited" (database check, R-OPS-038).
