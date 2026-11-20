---
id: R-LIB-017
level: 3
title: File name patterns
priority: should
status: verified
links:
  refines: [F-LIB-004]
  depends_on: [R-LIB-015]
  verified_by:
    - crates/musicus-api/src/import/pattern.rs::folder_preset
    - crates/musicus-api/src/import/pattern.rs::flat_number_preset_accepts_common_separators
    - crates/musicus-api/src/import/pattern.rs::flat_title_preset_with_and_without_number
    - crates/musicus-api/src/import/pattern.rs::values_are_cleaned_of_separators
    - crates/musicus-api/src/import/pattern.rs::custom_patterns
    - crates/musicus-api/src/import/pattern.rs::errors
    - crates/musicus-api/src/import/mod.rs::detection_picks_the_preset_that_parses_most_files
    - crates/musicus-api/src/import/mod.rs::detection_ties_are_decided_sensibly_and_deterministically
    - crates/musicus-api/src/import/review.rs::files_are_grouped_into_pieces
    - crates/musicus-api/src/import/review.rs::flat_files_group_by_number_and_need_a_title
  implemented_by:
    - crates/musicus-web/src/pages/import.rs
    - crates/musicus-api/src/import/pattern.rs
    - crates/musicus-api/src/import/mod.rs
    - crates/musicus-api/src/import/review.rs
---

# R-LIB-017 File name patterns

## Statement

The import shall read piece and part data from the file paths (relative to the selected folder) with a pattern made of the placeholders `{number}`, `{title}`, `{composer}`, `{arranger}`, `{genre}`, `{part}`, `{*}` (ignored text), optional segments `[…]` and literal text. Separators shall be tolerant: a space in the pattern also matches `_`, and values are trimmed of `-`, `–` and spaces at both ends. The presets shall describe general archive layouts, not the naming habits of one ensemble: "Folder per piece" `[{genre}/][{number} ]{title}[ - {composer}]/{part}.pdf` (default), "Number and part in the file name" `{number} {part}.pdf` and "Title and part in the file name" `[{number} ]{title} - {part}.pdf`. The import shall pre-select the preset that matches the most files (ties: more part names with a known instrument, then more part names understood completely, then the preset order), and shall let the librarian choose another preset or edit the pattern with a live preview. Files are grouped into pieces by archive number (leading zeros and separators ignored) or, without number, by title and composer.

## Rationale

Every ensemble names its files differently; a fixed structure would force librarians to rename thousands of files first.

## Acceptance criteria

- `Marches/0304 Alte Kameraden - Teike/Klarinette 1 in B.pdf` gives genre "Marches", number "0304", title "Alte Kameraden", composer "Teike", part "Klarinette 1 in B".
- `0304 Horn in F 1.pdf`, `0304_Horn_in_F_1.pdf` and `0304 - Horn in F 1.pdf` give number 0304 and the part "Horn in F 1" with the same preset.
- `0304 Radetzky March - Tuba.pdf` and `0304 - Radetzky March - Tuba.pdf` give number 0304, title "Radetzky March" and the part "Tuba"; for such files the title preset is pre-selected, for `0304 - Tuba.pdf` the number preset.
- Special naming (e.g. a counter between number and part) is read with an own pattern: `{number}Part{*}_{part}.pdf` reads `0304Part06_Clarinet 2.pdf` as number 0304, part "Clarinet 2".
- Files without a title in their names produce a piece with an empty title that must be typed once per piece.
- An invalid pattern (unknown placeholder, no `{part}`) is reported and not used.

## Notes

A pattern per subfolder (archives that mix structures) is planned for phase 2; today such archives are imported in several batches.
