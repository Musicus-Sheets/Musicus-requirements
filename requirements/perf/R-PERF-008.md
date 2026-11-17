---
id: R-PERF-008
level: 3
title: System detection budget
priority: should
status: implemented
links:
  refines: [F-PERF-001]
  implemented_by: [crates/musicus-server/src/layout/worker.rs, crates/musicus-server/src/layout/mod.rs]
  decided_in: [tech:d-system-layout]
---

# R-PERF-008 System detection budget

## Statement

The server shall detect the systems of an A4 page in at most 250 ms on one core of an x86-64 laptop (about one second on a Raspberry Pi 4), with one background worker, rendering at most 1754 × 1754 pixels per page, so that analysing a new file never delays requests.

## Acceptance criteria

- Measured on 226 pages of 23 real scores: 23–112 ms per page on average per file including rendering (AMD Ryzen 7 5800H, one core).
- Pages declaring a huge size (facsimiles) are rendered with the pixel budget of an A4 page at 150 dpi.

## Notes

Measured manually with `cargo run --release -p musicus-server --example layout_report`; no automated benchmark. Raspberry Pi value estimated (3–4× slower), not measured.
