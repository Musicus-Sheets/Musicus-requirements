---
id: R-FILE-003
level: 3
title: Page count and thumbnail
priority: must
status: verified
links:
  refines: [F-FILE-001]
  verified_by:
    - crates/musicus-server/src/processors.rs::reads_page_count_and_renders_thumbnail
    - crates/musicus-server/src/processors.rs::unreadable_pdf_is_kept_without_metadata
  implemented_by: [crates/musicus-server/src/processors.rs]
  decided_in: [tech:d-pdf-rendering]
---

# R-FILE-003 Page count and thumbnail

## Statement

When a PDF is uploaded, the system shall determine its page count and create a thumbnail of the first page; if the PDF cannot be analysed, it shall store the file anyway without this information.

## Acceptance criteria

- A 4-page PDF is listed with 4 pages and a thumbnail.
- A PDF the server cannot parse is stored and can be downloaded.
