---
id: R-OFF-001
level: 3
title: Encrypted local storage
priority: should
status: proposed
links:
  refines: [F-OFF-001]
---

# R-OFF-001 Encrypted local storage

## Statement

The app shall store sheets and annotations only encrypted, with a random key per device protected by the operating system's keystore.

## Acceptance criteria

- The app's data files cannot be read without the device keystore.

## Notes

App: Dioxus desktop/mobile (webview), reusing the web client's components and `musicus-api`. Local store options: SQLite with SQLCipher, or plain SQLite holding XChaCha20-Poly1305-encrypted blobs (RustCrypto). The data key is random per device and wrapped by the OS keystore (Android Keystore, iOS Keychain, Windows DPAPI, macOS Keychain).
