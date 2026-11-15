---
id: R-LIB-012
level: 3
title: Existing parts survive the change of part names
priority: must
status: verified
links:
  refines: [F-LIB-001]
  depends_on: [R-LIB-010, R-LIB-011, R-OPS-004]
  verified_by: [crates/musicus-server/tests/api.rs::migration_0002_keeps_old_parts]
  implemented_by:
    - crates/musicus-server/migrations/0002_part_names.sql
    - crates/musicus-server/src/part_index.rs
---

# R-LIB-012 Existing parts survive the change of part names

## Statement

When a database created before part names were derived is opened, the system shall keep every existing label as the custom name, keep numeric voices as text, convert key spellings that are unambiguous to the key codes, keep all other key values unchanged, and make the parts findable by name.

## Acceptance criteria

- Label "2nd Clarinet in Bb", voice 2, key "in Bb" becomes custom name "2nd Clarinet in Bb", voice "2", key code "Bb".
- An empty label becomes no custom name; "Es" becomes "Eb"; "B" and "Es/F" stay as they are.
- After the first start the library search finds old parts by their names.
