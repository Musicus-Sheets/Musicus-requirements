---
id: R-OPS-027
level: 3
title: Raspberry Pi
priority: must
status: accepted
links:
  refines: [F-OPS-006]
  depends_on: [R-OPS-028]
---

# R-OPS-027 Raspberry Pi

## Statement

The system shall run on a Raspberry Pi 3, 4, 5 or newer with a 64-bit operating system, both with Docker Compose and as a plain program.

## Acceptance criteria

- With 64-bit Raspberry Pi OS on a Pi 3 (1 GB), the published image and the arm64 program start and pass the smoke test.
- 32-bit systems and older models are not supported, and the user guide says so.

## Notes

Extends R-PERF-001 (Raspberry Pi 4) to the Pi 3; the performance targets have not been measured on a Pi 3 (or any Pi yet). Building Musicus on a Pi is not required: images and programs are built elsewhere. Snapshots (R-OPS-019) take space on the SD card.
