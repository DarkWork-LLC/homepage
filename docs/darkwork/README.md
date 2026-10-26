# Darkworks Lab

**Application:** Darkwork Labs
**Android package:** `com.darkworks.lab`
**Version:** 1.0.32
**Platforms:** Android and Linux
**Framework:** Flutter / Dart

Darkworks Lab is a local-first security monitoring application. It brings Bluetooth and network discovery, hardware telemetry, system monitoring, filesystem integrity scanning, and event logging into one responsive Flutter interface.

> **Educational use only:** This application is provided for learning, experimentation, and authorized defensive research. It is not professional security advice or a guarantee of protection. The developer assumes no responsibility or liability for any loss, damage, data loss, security incident, system change, or other consequence arising from use or inability to use this application. Use it only on systems and data you are authorized to inspect, and independently verify every result before taking action.

The current UI is a monitoring and inspection tool. It does not include a cloud backend, AI/LLM analysis, or a Windows target. Availability of individual sensors, network data, filesystem access, and SDR features depends on the platform and permissions.

## Features

- **Dashboard:** security status, perimeter scan trigger, Bluetooth/network counts, discovery overview, and theme toggle.
- **Device discovery:** Bluetooth/BLE and local network device lists with type filtering and refresh.
- **Network security:** network scanning, port/service assessment, security reports, and event logs.
- **Sensor monitor:** accelerometer, gyroscope, magnetometer, ambient light, battery, and location streams when available.
- **System monitor:** device information, CPU, memory, battery, network identity, sockets, and metric aggregates.
- **File integrity scan:** configurable scan setting (disabled by default) with MediaStore API integration coming in a future release. Shows disabled state with guidance when off.
- **Event logs:** locally retained application events with level-based display and date filtering.
- **Radio monitor:** SDR hardware detection and spectrum/status information.
- **Settings:** application settings and appearance controls exposed by the current UI.

## Architecture

The app uses Flutter Material 3 and Provider-based `ChangeNotifier` services:

- `SecurityService` — perimeter scanning and device discovery.
- `NetworkSecurityService` — network host, port, and security checks.
- `SensorService` — hardware sensor streams.
- `SystemMonitorService` — system and performance telemetry.
- `FilesystemScannerService` — local file scanning (MediaStore API, disabled by default).
- `RadioFrequencyService` — SDR detection and radio status.
- `LoggingService` and `DatabaseService` — local event/log persistence.
- `ThemeService` — light/dark Material 3 themes and shared colors.

Screens are under `lib/screens/`, reusable presentation is under `lib/widgets/`, and tests are under `test/`.

## Development

### Prerequisites

- Flutter 3.x with Dart 3.x
- Android toolchain for Android builds
- Linux GTK build dependencies for Linux builds

### Common commands

```bash
flutter pub get
flutter analyze
flutter test
flutter run -d android
flutter run -d linux
flutter build apk --debug
flutter build linux --debug
```

The repository also provides equivalent convenience targets in `Makefile` (for example `make get`, `make lint`, `make test`, and `make build-android`). The `Makefile` assumes Flutter is installed at `~/flutter/bin/flutter`; the direct Flutter commands above are portable when Flutter is on `PATH`.

## Platform and permissions

Android declares internet, network-state, Wi-Fi-state, Bluetooth, location, notification, and storage-related permissions in `android/app/src/main/AndroidManifest.xml`. The app follows the Google Play Store "All Files Access" policy and does **not** request `MANAGE_EXTERNAL_STORAGE`. Storage access is scoped to the MediaStore API via granular permissions (`READ_MEDIA_IMAGES/VIDEO/AUDIO` on Android 13+, `READ_EXTERNAL_STORAGE` on Android < 33) and is only requested at runtime when the user enables the **File Integrity Scan** core setting and initiates a scan. Scanning is disabled by default. Runtime location and Bluetooth permissions are requested on the first launch on supported mobile platforms. Linux has no Android permission dialogs; platform feature support varies by host and hardware.

## Documentation

- [User Guide](USER_GUIDE.md)
- [Privacy Policy](PRIVACY_POLICY.md)
- [Google Play Upload Guide](GOOGLE_PLAY_UPLOAD_GUIDE.md)
- [Release Summary](RELEASE_SUMMARY.md)
- [License](LICENSE.md)

## Ownership

Copyright © 2025–2026 Darkworks Lab and darkworkllc@gmail.com. Proprietary software; see [LICENSE.md](LICENSE.md).
