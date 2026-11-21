---
id: F-TECH-002
level: 2
title: Prepared for replacing storage and engines
priority: should
status: accepted
links:
  refines: [G-008]
---

# F-TECH-002 Prepared for replacing storage and engines

## Statement

The database, the file store and the PDF engine of the server are each used through one owned module, so that any of them could later be replaced without changing the rest of the program. No second implementation is built now.

## Rationale

Musicus is meant to be maintained for years by a small team (G-008). A switch to another database or to object storage is not planned, but it should stay a contained change instead of a rewrite.

## Notes

Does not change R-TECH-001: the server keeps using embedded SQLite. Replacing it would need a change of R-TECH-001 with the user's consent. Alternatives already evaluated: docs/agents/background.md §4 and §5.
