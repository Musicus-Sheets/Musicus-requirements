---
id: R-FILE-010
level: 3
title: Smaller scanned sheets
priority: could
status: proposed
links:
  refines: [F-PERF-002]
---

# R-FILE-010 Smaller scanned sheets

## Statement

When a scanned PDF is uploaded, the system shall offer to store an optimised version with bilevel image compression (CCITT G4 or JBIG2) if it is substantially smaller.

## Acceptance criteria

- A 10 MB colour scan of black-and-white music is reduced to a fraction of its size without visible loss of the notation.

## Notes

Scans range from about 0.1 MB per page (bilevel) to 1 MB per page (colour JPEG); the Wi-Fi, not the server, limits how fast a whole ensemble can load them (see F-PROG-002).
