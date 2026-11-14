---
id: R-SEC-002
level: 3
title: Secrets stored irreversibly
priority: must
status: implemented
links:
  refines: [F-SEC-002]
  implemented_by: [crates/musicus-server/src/auth.rs]
  decided_in: [tech:d-sessions, tech:d-hashing]
---

# R-SEC-002 Secrets stored irreversibly

## Statement

The system shall store passwords only as Argon2id hashes (19 MiB, 2 iterations, parallelism 1) and session and invite tokens (256-bit random) only as SHA-256 hashes.

## Acceptance criteria

- The database contains no plain password and no usable session token.
