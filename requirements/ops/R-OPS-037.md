---
id: R-OPS-037
level: 3
title: Unencrypted backups and exports with guidance
priority: must
status: accepted
links:
  refines: [F-OPS-002]
  conflicts_with:
    - id: R-ANN-018
      note: 'Backups, snapshots and exports are as readable as the database. Should annotations ever be encrypted at rest, they stay encrypted in these copies; the copies themselves are not encrypted again.'
---

# R-OPS-037 Unencrypted backups and exports with guidance

## Statement

Backups, snapshots and exports shall be written unencrypted, and the operating documentation shall state that they need the same protection as the data directory.

## Acceptance criteria

- The user guide's backup section says that a backup contains password hashes, all markings and all sheets, and must be stored as safely as the server itself.
- No backup, snapshot or export command asks for a password or key.

## Notes

The database is plain SQLite; passwords are stored only as Argon2 hashes (d-hashing).
