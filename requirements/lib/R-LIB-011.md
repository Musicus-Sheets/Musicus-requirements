---
id: R-LIB-011
level: 3
title: Keys from a fixed list
priority: should
status: verified
links:
  refines: [F-LIB-001]
  verified_by:
    - crates/musicus-api/src/naming.rs::keys
    - crates/musicus-server/tests/api.rs::part_names_keys_and_part_search
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-api/src/naming.rs
    - crates/musicus-server/src/routes/library.rs
    - crates/musicus-web/src/pages/forms.rs
---

# R-LIB-011 Keys from a fixed list

## Statement

The system shall accept as key of a part only none (concert pitch) or one of B♭, E♭, F, C, A, D, G, E, A♭, D♭, G♭ and B♮ (H), stored as the codes Bb, Eb, F, C, A, D, G, E, Ab, Db, Gb and H, and the web client shall offer exactly these in a selection list.

## Acceptance criteria

- The key field of the part forms is a selection list; it shows the keys with ♭ and ♮ signs.
- Through the API, unambiguous spellings such as "in B-flat", "B♭" or the German "Es" are stored as the code; an unknown key, and the ambiguous "B" (B♭ in German, B♮ in English), are rejected with HTTP 400.
- A part whose stored key is not in the list (older data) keeps it when it is saved unchanged; the web client offers it as "Other: …".
