---
id: R-ANN-007
level: 3
title: Compact storage
priority: should
status: verified
links:
  refines: [F-ANN-003]
  constrains: [R-ANN-010]
  verified_by: [crates/musicus-api/src/ink.rs::typical_page_stays_small]
  implemented_by: [crates/musicus-api/src/ink.rs]
  decided_in: [tech:d-ink-format]
---

# R-ANN-007 Compact storage

## Statement

The system shall store a typical annotated page (30 strokes of 60 points) in less than 12 KB before compression.

## Acceptance criteria

- The unit test for a typical page stays below 12 000 bytes.
