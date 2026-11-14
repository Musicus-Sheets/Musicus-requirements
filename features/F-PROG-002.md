---
id: F-PROG-002
level: 2
title: Prepare a programme in advance
priority: must
status: implemented
links:
  refines: [G-004]
  depends_on: [F-PROG-001]
  conflicts_with:
    - id: F-SEC-001
      note: 'Prefetched sheets are held in memory only, never stored on the device; a reload downloads them again.'
---

# F-PROG-002 Prepare a programme in advance

## Statement

When a member opens a programme, all their sheets of it are downloaded ahead of time, so that playing needs no network.

## Rationale

The rehearsal-room Wi-Fi, not the server, is the bottleneck when everyone opens the same piece (60 musicians x 3 MB take 7–30 s over typical Wi-Fi).
