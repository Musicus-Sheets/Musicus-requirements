---
id: R-OPS-035
level: 3
title: Version on the documentation
priority: must
status: implemented
links:
  refines: [F-OPS-007]
  implemented_by:
    - docs/user-guide/main.typ
    - docs/user-guide/build.sh
    - docs/technical/main.typ
    - docs/technical/build.sh
    - scripts/build-guide-site.sh
---

# R-OPS-035 Version on the documentation

## Statement

The user guide and the technical documentation of a release shall name that release's version on their title page, and the user guide site shall name it on every page.

## Acceptance criteria

- The title page of the user guide PDF and of the technical documentation PDF, and the head of their HTML pages, show the release version (for example "Musicus 1.2").
- Every page of the user guide site shows the version it belongs to.
- The release check fails if the version on a title page differs from the release version: stage 1 of the release pipeline (R-OPS-049) builds both documents and checks their title pages before anything is published, in addition to checking that the workspace version equals the version in the release branch name.

## Notes

Both title pages take the version from their build (`build.sh [version]` → `typst --input
version=…`; else `$MUSICUS_VERSION`, else the workspace version of the main repository's
`Cargo.toml`, else "dev"). The guide site passes each release's workspace version and shows
the release in its version bar on every page; it warns when a release tag differs from the
workspace version at that tag; for older releases this stays a warning. Open: the check in stage 1
of the release pipeline (R-OPS-049) that fails on a difference; until then the warning of the
guide site and the release checklist in `RELEASING.md` are the only checks.
