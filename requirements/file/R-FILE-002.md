---
id: R-FILE-002
level: 3
title: File versions
priority: must
status: verified
links:
  refines: [F-FILE-001]
  depends_on: [R-FILE-004]
  verified_by:
    - crates/musicus-server/tests/api.rs::uploads_are_versioned_and_validated
  implemented_by: [crates/musicus-server/src/routes/library.rs]
---

# R-FILE-002 File versions

## Statement

When a librarian uploads a file with different content for a part, the system shall add it as a new version and keep all previous versions readable; uploading the current content again shall not create a version.

## Acceptance criteria

- Uploading a corrected PDF turns version 1 into version 2; version 1 can still be downloaded.
- Uploading the same PDF twice leaves the part at version 1.
