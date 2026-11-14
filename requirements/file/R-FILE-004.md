---
id: R-FILE-004
level: 3
title: 'Immutable, content-addressed storage'
priority: must
status: verified
links:
  refines: [F-FILE-001, F-OPS-002]
  verified_by: [crates/musicus-server/src/blobs.rs::stores_by_hash_and_deduplicates]
  implemented_by: [crates/musicus-server/src/blobs.rs]
  decided_in: [tech:d-blobs]
---

# R-FILE-004 Immutable, content-addressed storage

## Statement

The system shall store every file once under its SHA-256 hash, never modify or overwrite a stored file, and write it so that a stored file is always complete.

## Acceptance criteria

- Uploading identical content twice results in one file on disk.
- An interrupted upload leaves no file in the store.
