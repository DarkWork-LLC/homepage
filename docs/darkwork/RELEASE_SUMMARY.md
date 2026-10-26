# Darkworks Lab Release Summary

**Package:** `com.darkworks.lab`
**Version:** 1.0.32
**Release target:** Android; Linux is also present as a desktop target
**Privacy model:** local-first monitoring

> **Educational use only:** This release is for learning, experimentation, and authorized defensive research. The developer assumes no responsibility or liability for any loss, damage, data loss, security incident, system change, or other consequence arising from use or inability to use this application.

## Current scope

This release provides a Flutter Material 3 interface for:

- Dashboard status, perimeter scan trigger, Bluetooth/network counts, and theme switching.
- Bluetooth and local network device discovery and filtering.
- Network host/port scanning, security reports, and event logs.
- Hardware sensor monitoring where supported.
- System, memory, battery, network identity, socket, and aggregate telemetry.
- Configurable file integrity scan setting (disabled by default). Scanning uses the MediaStore API when enabled — no All Files Access permission is requested. Scanning logic is currently commented out pending the MediaStore integration, which will be completed in a future release.
- Local event logs and application settings.

The dashboard environment-alert area currently presents a secure empty state. AI/Intelligence screens and related provider wiring remain commented out and are not user-accessible features in this release.

## Platform notes

Android is the publishing target. Linux is a supported Flutter desktop build target in the repository but has different permissions and hardware availability. The current app does not include Windows-specific source, IOS, or a cloud backend (yet).

## Privacy and safety

The app is designed to process monitoring data on the device. Permissions and feature availability vary by platform. Results are diagnostic and may be incomplete because of inaccessible files, unavailable sensors, permissions, network configuration, or unsupported SDR hardware. Users must review findings before taking action.
```

See [README.md](README.md), [USER_GUIDE.md](USER_GUIDE.md), and [PRIVACY_POLICY.md](PRIVACY_POLICY.md) for current usage and privacy details.

## Release notes for Google Play

**Version 1.0.32 — Scoped Storage & MediaStore Migration**

This release migrates file access from All Files Access (`MANAGE_EXTERNAL_STORAGE`) to the MediaStore API, in compliance with the Google Play Store policy.

- **Storage permissions** changed to granular `READ_MEDIA_IMAGES`, `READ_MEDIA_VIDEO`, and `READ_MEDIA_AUDIO` (Android 13+) and `READ_EXTERNAL_STORAGE` (Android < 33). `MANAGE_EXTERNAL_STORAGE` and `WRITE_EXTERNAL_STORAGE` are no longer requested.
- **File Integrity Scan** is now a configurable core setting, disabled by default to comply with the "No Access to Files" policy. It can be enabled in Settings.
- Storage permissions are no longer requested at startup — they are only requested when the user enables file scanning and initiates a scan.
- File scanning logic is temporarily disabled (commented out) while the MediaStore integration is completed. The scanning UI now shows a clear disabled state with guidance to enable the setting.
- Added `contentUri` support to `FileScanResult` for future MediaStore-based queries and deletion.
- Updated Privacy Policy and Google Play Upload Guide to reflect scoped storage changes.
