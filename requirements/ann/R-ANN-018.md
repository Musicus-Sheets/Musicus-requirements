---
id: R-ANN-018
level: 3
title: Encrypted annotations at rest
priority: could
status: proposed
links:
  refines: [F-ANN-004]
---

# R-ANN-018 Encrypted annotations at rest

## Statement

The system shall store annotation layers encrypted with a key per user, so that access to the database file alone does not reveal them.

## Acceptance criteria

- The annotation data in the database file cannot be decoded without the user's key.
