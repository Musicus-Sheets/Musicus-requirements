---
id: R-LIB-022
level: 3
title: Further import sources (OCR, inventory list)
priority: could
status: proposed
links:
  refines: [F-LIB-004]
  depends_on: [R-LIB-019]
---

# R-LIB-022 Further import sources (OCR, inventory list)

## Statement

The import shall add candidates for title, composer, arranger, archive number and instrument from text recognised on the first page of each file (OCR) and from an inventory list of the archive (CSV), each marked with its source, in the same review and with the same colours as the values read from file names.

## Rationale

Scans named "Scan_0001.pdf" carry no information in their names; many archives keep a spreadsheet of their folders.

## Acceptance criteria

- A file whose name gives no title gets the title printed on its first page as a yellow candidate with source "ocr".
- A CSV line "0304;Alte Kameraden;Teike" fills title and composer of piece 0304 with source "inventory".

## Notes

The review data already stores every value with its source (`pattern`, `dictionary`, `alias`, `library`, `librarian`; reserved: `ocr`, `inventory`), so new sources add candidates without changing the workflow.
