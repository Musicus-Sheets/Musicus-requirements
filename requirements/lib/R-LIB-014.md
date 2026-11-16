---
id: R-LIB-014
level: 3
title: Suggestions of existing tags and families
priority: should
status: verified
links:
  refines: [F-LIB-001]
  depends_on: [R-LIB-013, R-ACL-001]
  verified_by:
    - e2e/smoke.mjs
    - crates/musicus-server/tests/api.rs::programmes_and_search
  implemented_by:
    - crates/musicus-web/src/suggest.rs
    - crates/musicus-web/src/tag_input.rs
    - crates/musicus-web/src/pages/instruments.rs
    - crates/musicus-server/src/routes/library.rs
---

# R-LIB-014 Suggestions of existing tags and families

## Statement

While a librarian types a tag of a piece or the family of an instrument, the web client shall show a small list of the existing tags or families that match the typed text, ignoring letter case and diacritics, those starting with the text first, without the tags the piece already has.

## Acceptance criteria

- Typing "fete" in the tag field suggests the existing tag "Fête"; typing "BRA" in the family field suggests "Brass".
- ↓ / ↑ choose a suggestion, Enter or Tab take it (a taken tag becomes a chip; Enter does not submit the form), Escape closes the list, a click or tap takes a suggestion.
- A tag the piece already has is not suggested.
- `GET /api/tags` returns every tag to librarians and only the tags of scores a member can see to members.
