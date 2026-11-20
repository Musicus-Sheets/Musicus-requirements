---
id: R-LIB-010
level: 3
title: Part names derived from instruments, key and voices
priority: should
status: verified
links:
  refines: [F-LIB-001]
  depends_on: [R-LIB-002, R-LIB-011]
  verified_by:
    - crates/musicus-api/src/naming.rs::derived_names
    - crates/musicus-api/src/naming.rs::custom_name_wins
    - crates/musicus-api/src/naming.rs::natural_order
    - crates/musicus-api/src/naming.rs::several_voices_are_joined_in_order
    - crates/musicus-server/tests/api.rs::parts_with_several_voices
    - crates/musicus-server/tests/api.rs::part_names_keys_and_part_search
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-api/src/naming.rs
    - crates/musicus-server/src/routes/library.rs
    - crates/musicus-web/src/pages/forms.rs
    - crates/musicus-web/src/names.rs
    - crates/musicus-i18n/locales/en/names.ftl
---

# R-LIB-010 Part names derived from instruments, key and voices

## Statement

When a part has no custom name, the system shall name it after its instruments, key and voices in the form "<instruments joined by ' / ' in alphabetical order> in <key> <voices joined by ' & ' in their order>", and shall show this name, or the custom name if one is given, wherever the part is shown.

## Acceptance criteria

- Trumpet, B♭, voice 1 gives "Trumpet in B♭ 1"; Klarinette with voices 1 and 2 gives "Klarinette 1 & 2"; Flöte and Oboe with voices 1 and 2 give "Flöte / Oboe 1 & 2"; voices 1, 2, 3 give "… 1 & 2 & 3"; Flute and Piccolo without key and voice give "Flute / Piccolo"; voice 2 without instrument and key gives "Part 2"; nothing at all gives "Unnamed part".
- A custom name ("Solo Cornet") replaces the derived name; clearing it brings the derived name back.
- Renaming an instrument renames the derived names of its parts.
- The web client composes the name in the user interface language from the components the server sends (R-I18N-006); the parts of a score are listed by name, numbers by value ("… 2" before "… 10"); parts with several voices by their first voice, then the next ("… 1", "… 1 & 2", "… 2").
- While adding or editing a part, the web client shows the resulting name live and offers the derived name as placeholder of "Custom name (optional)".
