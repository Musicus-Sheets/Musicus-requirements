---
id: R-OPS-014
level: 3
title: Downgrade window
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  depends_on: [R-OPS-018]
  decided_in: [tech:d-update-model]
---

# R-OPS-014 Downgrade window

## Statement

When an older release is started on a data directory last used by a newer release, the system shall start and keep the data if the older release is (a) of one of the three minor releases before the newer one, (b) the release the installation was upgraded from, within three months after that upgrade, or (c) of the same minor release as the newer one.

## Acceptance criteria

- 1.5.x to 1.2.x, 1.3.x and 1.4.x: the older release starts (a).
- An installation upgraded from 1.0.3 to 1.5.0: 1.0.3 starts on it during the three months after that upgrade; afterwards only 1.2.x to 1.4.x start (b).
- 1.5.7 to 1.5.0 and back: always possible, however many patch releases lie between (c).
- 1.5.x to 1.1.x without an upgrade from 1.1.x within three months: refused as in R-OPS-015.
- The three months are counted from the start of the newer release that performed the upgrade; the time is stored in the database, not taken from file dates.

## Notes

Interpretations to confirm: "minor release" means a release line X.Y counted in release order across major versions (so 2.0 follows 1.9), and any patch release of such a line may be started; with several upgrades in a row (1.0 → 1.5 → 1.6) each release the installation was upgraded from stays a target for three months after that upgrade. Changes that restrict access may shorten the window (R-OPS-017).
