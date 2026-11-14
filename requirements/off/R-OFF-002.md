---
id: R-OFF-002
level: 3
title: Synchronisation
priority: should
status: proposed
links:
  refines: [F-OFF-001]
  depends_on: [R-FILE-004, R-ANN-012]
---

# R-OFF-002 Synchronisation

## Statement

The app shall synchronise sheets by file hash and annotations by page revision, transferring only what changed.

## Acceptance criteria

- A second sync without changes transfers no file contents.

## Notes

Files: the client sends the hashes it has; the server answers with what it may and should have; unchanged files are never transferred again. Annotations: step 1 is a per-object merge (object ids, tombstones for deletions, last writer wins per object), enough because only one person edits a set; step 2, only if needed, per-set CRDT documents (Loro or Automerge). Server work: a `/sync` endpoint and a per-user change feed (server revision counter); both can be added without migrating existing data.
