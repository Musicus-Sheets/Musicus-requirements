---
id: R-OPS-049
level: 3
title: Release pipeline publishes only when everything succeeded
priority: must
status: accepted
links:
  refines: [F-OPS-005, F-OPS-006, F-OPS-007]
  depends_on: [R-OPS-028, R-OPS-029, R-OPS-032, R-OPS-035, R-OPS-040]
---

# R-OPS-049 Release pipeline publishes only when everything succeeded

## Statement

A release shall be built, checked and published by one automated pipeline that publishes nothing unless every build and check of the release succeeded.

## Acceptance criteria

- On a pull request from `release/<version>` the pipeline runs as a dry run: everything is built and checked, nothing is published.
- Merging a `release/<version>` pull request into `main` starts the real run automatically.
- Stage 1 produces only temporary results (workflow artifacts that expire): the workspace version in `Cargo.toml` equals the version in the branch name; all tests, lints, documentation and requirements checks pass; the database release check passes (R-OPS-040); the program is built and smoke-tested per platform (R-OPS-029, R-OPS-032); the multi-arch container images are built but not pushed (R-OPS-028); the user guide and the technical documentation are built and their title pages show the release version (R-OPS-035); the complete user guide website including the new release is built.
- Stage 2 runs only if stage 1 succeeded completely, in this order (least reversible last): push the images with their version tags, create the tag `vX.Y.Z` in the main repository, create the GitHub release with the program archives and `SHA256SUMS`, deploy the user guide website.
- Every stage 2 step is idempotent: a failed publish run can be re-run and completes what is missing without duplicating what exists.
- If anything fails, nothing is published, the artifacts are discarded, and after a fix the pipeline is run again.

## Notes

User decision. The existing website workflow (`user-guide-pages.yml`, started by a published release) becomes the last step of this pipeline; its manual test-build mode stays. The tags of the documentation repositories (R-OPS-036) are created by hand after the pipeline succeeded. Until the pipeline exists, the maintainer follows the manual steps in `RELEASING.md`.
