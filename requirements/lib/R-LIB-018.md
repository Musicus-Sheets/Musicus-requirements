---
id: R-LIB-018
level: 3
title: Part names in file names
priority: should
status: verified
links:
  refines: [F-LIB-004]
  depends_on: [R-LIB-010, R-LIB-011, R-LIB-003, R-LIB-002]
  verified_by:
    - crates/musicus-api/src/import/parts.rs::german_and_english_names
    - crates/musicus-api/src/import/parts.rs::no_key_is_ever_assumed
    - crates/musicus-api/src/import/parts.rs::german_letters_only_in_german_batches
    - crates/musicus-api/src/import/parts.rs::partitur_and_direktion_are_different_instruments
    - crates/musicus-api/src/import/parts.rs::levels_of_instrument_words
    - crates/musicus-api/src/import/parts.rs::language_suggestion
    - crates/musicus-api/src/import/parts.rs::several_voices
    - crates/musicus-api/src/import/parts.rs::an_instrument_named_twice_is_listed_once
    - crates/musicus-api/src/import/review.rs::partitur_and_direktion_need_their_own_instruments
  implemented_by:
    - crates/musicus-api/src/import/parts.rs
---

# R-LIB-018 Part names in file names

## Statement

The import shall read instrument(s), key and voices from the part text of a file name in any order, in German or English, with common abbreviations and without spaces (`Klarinette 2 in B`, `Bb Clarinet II`, `Klar2B`, `KlarinetteEb`, `Trp 1`, `Pos. 3`). A part may contain several voices (R-LIB-002): voices joined by `+`, `&`, `/`, `,`, `und` or `and` (`Trompete 1+2`, `1/2`, `1 & 2`, `I+II`) shall give the voices "1" and "2" in the order written; voices that only stand next to each other (`Trompete 1 2`) shall also be read as several voices but flagged for review, as the second number may be a copy or page number. It shall never assume a key: a name without key gives no key. German key names (`B` = B♭, `Es`, `As`, `Des`, `Ges`, `H` = B♮) shall be read only when the batch's naming language is German; the language shall be suggested from the instrument words found. A letter that is ambiguous in the batch's language shall be flagged for review and left empty. "Partitur" (full score; also "Score", "Full score") and "Direktion" (also "Direction", "Dirigierstimme", "Conductor", "Conductor score", "Condensed score") shall be two different instruments. Abbreviations and guessed words shall be flagged for review. An instrument named several times in one part name (full word and abbreviation, German and English word) shall be read once, at its first place.

## Rationale

The instrument decides who may read a part (R-ACL-001); the key is part of the part's name (R-LIB-010). A guessed key or a full score shown as conductor's part would put wrong sheets in front of musicians.

## Acceptance criteria

- `Klarinette 1` gives instrument Clarinet, voice 1 and no key.
- `Trompete 1+2`, `Trompete 1/2`, `Trompete 1 & 2` and `Trompete I+II` give the voices 1 and 2 without a flag (name "Trumpet 1 & 2"); `Trompete 1 2` gives the voices 1 and 2, flagged for review.
- In a German batch `Klarinette 2 in B` gives key B♭; in an English batch the key is empty and flagged.
- `Partitur.pdf` and `Direktion.pdf` of one piece become parts of two different instruments.
- `Klarinette Klar 1` and `Trp/Trompete 1` give one instrument each (Clarinet, Trumpet), not two.
