---
id: F-LIB-004
level: 2
title: Mass import of a sheet archive
priority: should
status: implemented
links:
  refines: [G-001]
---

# F-LIB-004 Mass import of a sheet archive

## Statement

Librarians can bring an existing digital archive (a folder tree of PDF files, hundreds to thousands of pieces) into the library in one go: Musicus reads number, title, composer, category and the part (instrument, key, voice) from the folder and file names, shows a proposal for review, and creates pieces and parts only after the librarian has checked and committed them.

## Rationale

Ensembles that switch to Musicus usually have years of scanned parts on a disk. Entering them piece by piece through the piece form would take weeks; a wrong automatic import would put parts with the wrong instrument in front of the wrong musicians (the instrument decides who reads a part, F-ACL-001).

## Notes

Phase 1 reads folder structure and file names only. Text recognition on the first page (OCR) and an inventory list (CSV) are planned as further sources of the same proposals (R-LIB-022).
