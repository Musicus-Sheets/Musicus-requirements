---
id: R-LIB-016
level: 3
title: Import a folder of PDF files
priority: should
status: verified
links:
  refines: [F-LIB-004]
  depends_on: [R-FILE-001, R-FILE-004, R-ACL-001, R-SEC-001]
  verified_by:
    - e2e/smoke.mjs
    - crates/musicus-server/tests/api.rs::import_stages_reviews_commits_and_undoes
    - crates/musicus-server/tests/api.rs::import_of_flat_numbered_files_groups_by_number_and_keeps_changes
  implemented_by:
    - crates/musicus-web/src/pages/import.rs
    - crates/musicus-web/src/pages/import_review.rs
    - crates/musicus-web/src/bridge.rs
    - crates/musicus-web/js/bridge.js
    - crates/musicus-server/src/routes/import.rs
    - crates/musicus-server/migrations/0007_import.sql
  decided_in: [tech:d-import-staging]
---

# R-LIB-016 Import a folder of PDF files

## Statement

The system shall let a librarian select a folder (or drop it onto the import page) and upload every PDF file in it and its subfolders into a staging area of an import batch, ignoring other files. The browser shall compute the SHA-256 of each file before uploading; files whose content is already in the library or already in the batch shall be skipped and never imported twice. Selecting the same folder again shall continue an interrupted import without uploading finished files again. Staged files shall not be readable by anyone through the library until they are committed (R-LIB-021); nothing shall be stored on the device.

## Rationale

Archives are large and uploads get interrupted; re-running an import must be safe. Staged files may still carry wrong instruments and must not reach members before a librarian has checked them.

## Acceptance criteria

- Only librarians and admins can use the import (members get HTTP 403).
- A file whose content was uploaded before is reported as duplicate and not uploaded again; of two files with the same content in one folder, the first path (in alphabetical order) is imported.
- After uploading half of a folder and selecting it again, only the missing files are uploaded.
- A staged file is not served by `/api/files/{sha256}` (404), also not to a librarian, until its part is committed.
