---
id: R-OPS-029
level: 3
title: Program files for every supported system
priority: should
status: accepted
links:
  refines: [F-OPS-006]
  depends_on: [R-OPS-026, R-OPS-030]
---

# R-OPS-029 Program files for every supported system

## Statement

Each published release shall offer a ready-to-run program archive, built by the continuous integration, for every system and architecture of R-OPS-026 and R-OPS-042, together with a `SHA256SUMS` file.

## Acceptance criteria

- The release page offers `linux-x86_64`, `linux-arm64`, `windows-x86_64` (`.zip`), `macos-arm64` and `macos-x86_64` (R-OPS-042) archives, all built by CI, not by hand.
- `sha256sum -c SHA256SUMS` in the download folder succeeds for every archive.
- A downloaded program starts without installing Rust or other build tools.
- The user guide explains the first start of an unsigned download: Windows SmartScreen ("Windows protected your PC" → "More info" → "Run anyway"; typically only when double-clicking a downloaded file in Explorer, usually not when started from a terminal or as a service) and macOS Gatekeeper ("cannot be verified" → right-click → Open, or allow it in System Settings → Privacy & Security).

## Notes

The programs are unsigned for now (user decision). Signing is possible later: Windows with a code-signing certificate, Microsoft Trusted Signing, or free signing for open-source projects via the SignPath Foundation; macOS with the Apple Developer Program (about 99 USD per year) and notarisation. A macOS x86_64 build that fails does not block the release (R-OPS-042).
