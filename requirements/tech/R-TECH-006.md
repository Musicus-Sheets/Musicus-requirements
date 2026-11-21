---
id: R-TECH-006
level: 3
title: PDF engine behind one module
priority: should
status: accepted
links:
  refines: [F-TECH-002]
---

# R-TECH-006 PDF engine behind one module

## Statement

The server shall use its PDF library only through one module that offers page count, thumbnail and page rendering.

## Acceptance criteria

- Only that module imports the PDF library (today hayro).

## Notes

The web client's pdf.js is already behind `bridge.rs` (d-pdf-rendering).
