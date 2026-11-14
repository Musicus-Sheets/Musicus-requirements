---
id: R-FILE-001
level: 3
title: Accepted uploads
priority: must
status: verified
links:
  refines: [F-FILE-001]
  verified_by:
    - crates/musicus-server/tests/api.rs::uploads_are_versioned_and_validated
    - crates/musicus-server/src/blobs.rs::rejects_oversized_bodies_and_cleans_up
    - crates/musicus-server/src/processors.rs::sniffs_pdf_only
  implemented_by:
    - crates/musicus-server/src/routes/library.rs
    - crates/musicus-server/src/processors.rs
    - crates/musicus-server/src/blobs.rs
---

# R-FILE-001 Accepted uploads

## Statement

The system shall accept as part file only PDF files (recognised by their content) up to a configurable size, by default 200 MB.

## Acceptance criteria

- Uploading an XML file is rejected with HTTP 415.
- Uploading a file larger than the limit is rejected with HTTP 413 and leaves no temporary file behind.
