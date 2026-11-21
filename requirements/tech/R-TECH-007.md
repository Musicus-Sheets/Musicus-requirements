---
id: R-TECH-007
level: 3
title: Conformance tests for replaceable parts
priority: should
status: accepted
links:
  refines: [F-TECH-002]
  depends_on: [R-TECH-004, R-TECH-005, R-TECH-006]
---

# R-TECH-007 Conformance tests for replaceable parts

## Statement

The storage modules, the file store and the PDF engine shall each have a test suite that states the behaviour any replacement must keep.

## Acceptance criteria

- The storage suite checks the access rule on a fixed set of users, groups and grants.
- The file store suite checks content addressing, atomic writes, immutability and deduplication.
- The PDF engine suite checks page counts and rendering of fixture PDFs.
