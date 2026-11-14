---
id: R-READ-006
level: 3
title: Compatible PDF rendering
priority: must
status: verified
links:
  refines: [F-READ-001]
  constrains: [R-READ-001]
  verified_by: [e2e/smoke.mjs]
  implemented_by: [scripts/fetch-pdfjs.sh, crates/musicus-web/js/bridge.js]
  decided_in: [tech:d-pdf-rendering]
---

# R-READ-006 Compatible PDF rendering

## Statement

The web client shall render PDF pages with a build of pdf.js that also works in older tablet browsers.

## Acceptance criteria

- Pages render in Chromium versions without Map.prototype.getOrInsertComputed.
