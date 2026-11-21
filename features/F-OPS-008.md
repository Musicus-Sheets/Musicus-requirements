---
id: F-OPS-008
level: 2
title: Open devices survive restarts and updates
priority: must
status: accepted
links:
  refines: [G-004, G-005]
  depends_on: [F-OPS-005]
---

# F-OPS-008 Open devices survive restarts and updates

## Statement

When the server stops, is unreachable, starts or comes back with a new version, the tablets and computers that have Musicus open tell their users what is happening in plain words, keep showing what is already loaded, keep unsaved markings in memory and save them as soon as the server is back, and switch to a new version only at a moment when nobody is reading or drawing.

## Rationale

Tablets stay open on the music stands for hours. An update or a restart of the server (G-005) must not cost a marking or interrupt a musician who is playing (G-004), and a vague error message would make volunteers think Musicus is broken.

## Notes

Nothing is stored on the device (R-SEC-001): unsaved markings live only in the open tab. Plan: docs/technical chapter "Updates, downgrades and platforms", section on open clients.
