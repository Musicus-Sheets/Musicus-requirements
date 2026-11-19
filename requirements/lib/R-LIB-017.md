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
    - crates/musicus-api/src/import/pattern.rs::flat_number_preset_ignores_counters
    - crates/musicus-api/src/import/pattern.rs::flat_title_and_category
    - crates/musicus-api/src/import/pattern.rs::custom_patterns
    - crates/musicus-api/src/import/pattern.rs::errors
    - crates/musicus-api/src/import/mod.rs::detection_picks_the_preset_that_parses_most_files
    - crates/musicus-api/src/import/review.rs::files_are_grouped_into_pieces
    - crates/musicus-api/src/import/review.rs::flat_files_group_by_number_and_need_a_title
  implemented_by:
    - crates/musicus-api/src/import/pattern.rs
    - crates/musicus-api/src/import/mod.rs
    - crates/musicus-api/src/import/review.rs
---

# R-LIB-017 File name patterns

## Statement

The import shall read piece and part data from the file paths (relative to the selected folder) with a pattern made of the placeholders `{number}`, `{title}`, `{composer}`, `{arranger}`, `{genre}`, `{part}`, `{*}` (ignored text), optional segments `[…]` and literal text. It shall offer the presets "Folder per piece" `[{genre}/][{number} ]{title}[ - {composer}]/{part}.pdf` (default), "Category / piece" `{genre}/[{number} ]{title}[ - {composer}]/{part}.pdf`, "One folder, title in the file name" `{title} - {part}.pdf` and "One folder, archive number in the file name" `{number}Stimme{*}_{part}.pdf`, shall pre-select the preset that matches the most files, and shall let the librarian choose another preset or edit the pattern with a live preview. Files are grouped into pieces by archive number (leading zeros and separators ignored) or, without number, by title and composer.

## Rationale

Every ensemble names its files differently; a fixed structure would force librarians to rename thousands of files first.

## Acceptance criteria

- `Marches/0304 Alte Kameraden - Teike/Klarinette 1 in B.pdf` gives genre "Marches", number "0304", title "Alte Kameraden", composer "Teike", part "Klarinette 1 in B".
- `304Stimme06_Klarinette2.pdf` and `302Stimme-06_Klarinette2.pdf` give numbers 304 and 302 and the part "Klarinette2"; "Stimme06" is ignored.
- Files without a title in their names produce a piece with an empty title that must be typed once per piece.
- An invalid pattern (unknown placeholder, no `{part}`) is reported and not used.

## Notes

A pattern per subfolder (archives that mix structures) is planned for phase 2; today such archives are imported in several batches.
