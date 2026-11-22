---
id: R-OPS-014
level: 3
title: Downgrade window
priority: must
status: implemented
links:
  refines: [F-OPS-005]
  depends_on: [R-OPS-018]
  decided_in: [tech:d-update-model]
  implemented_by:
    - crates/musicus-server/src/updates/window.rs
    - crates/musicus-server/src/updates/runner.rs
    - crates/musicus-server/migrations/releases.txt
  verified_by:
    - crates/musicus-server/src/updates/window.rs::upgrade_source_stays_a_target_for_three_months
    - crates/musicus-server/src/updates/window.rs::previous_lines_count_in_release_order
    - crates/musicus-server/src/updates/window.rs::chained_upgrades
    - crates/musicus-server/src/updates/window.rs::patches_of_the_same_line
    - crates/musicus-server/tests/updates.rs::removal_runs_only_when_due_and_older_releases_are_then_refused
    - crates/musicus-server/tests/updates.rs::patches_of_the_same_line_replace_each_other
---

# R-OPS-014 Downgrade window

## Statement

When an older release is started on a data directory last used by a newer release, the system shall start and keep the data if the older release is (a) of one of the three minor releases before the newer one, (b) the release the installation was upgraded from, within three months after that upgrade, or (c) of the same minor release as the newer one.

## Acceptance criteria

- 1.5.x to 1.2.x, 1.3.x and 1.4.x: the older release starts (a).
- An installation upgraded from 1.0.3 to 1.5.0: 1.0.3 starts on it during the three months after that upgrade; afterwards only 1.2.x to 1.4.x start (b).
- 1.5.7 to 1.5.0 and back: always possible, however many patch releases lie between (c).
- 1.5.x to 1.1.x without an upgrade from 1.1.x within three months: refused as in R-OPS-015.
- Release order, not numbering: with 1.8 → 1.9 → 1.10 → 2.0 released in that order, the targets from 2.0 are 1.10, 1.9 and 1.8 (a).
- Chained upgrades 1.0 → 1.5 → 1.6: 1.0 stays a target for three months after the upgrade to 1.5, and 1.5 for three months after the upgrade to 1.6 (b), besides the three minors.
- The three months are counted from the start of the newer release that performed the upgrade; the time is stored in the database, not taken from file dates.

## Notes

Confirmed by the user: "the three previous minor releases" are the three release lines (X.Y) released before the current one, in release order, regardless of their numbers (1.10 may follow 1.9, and 2.0 then follows 1.10, not 1.9); any patch release of such a line may be started. With several upgrades in a row, each release the installation was upgraded from stays a target for three months after its own upgrade. The window always holds and is never shortened, also not by restrictions of access (R-OPS-017).
