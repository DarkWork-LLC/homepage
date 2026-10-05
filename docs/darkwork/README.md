# Darkworks Lab

**Application:** Darkworks Lab
**Android package:** `com.darkworks.lab`
**Version:** 1.0.0+1
**Platforms:** Android and Linux

Darkworks Lab is a local-first security monitoring application. It brings Bluetooth and network discovery, hardware telemetry, system monitoring, filesystem integrity scanning, and event logging into one responsive interface.

> **Educational use only:** This application is provided for learning, experimentation, and authorized defensive research. It is not professional security advice or a guarantee of protection. The developer assumes no responsibility or liability for any loss, damage, data loss, security incident, system change, or other consequence arising from use or inability to use this application. Use it only on systems and data you are authorized to inspect, and independently verify every result before taking action.

The current UI is a monitoring and inspection tool. Availability of individual sensors, network data, filesystem access, and SDR features depends on the platform and permissions.

## Features

- **Dashboard:** security status, perimeter scan trigger, Bluetooth/network counts, discovery overview, and theme toggle.
- **Device discovery:** Bluetooth/BLE and local network device lists with type filtering and refresh.
- **Network security:** network scanning, port/service assessment, security reports, and event logs.
- **Sensor monitor:** accelerometer, gyroscope, magnetometer, ambient light, battery, and location streams when available.
- **System monitor:** device information, CPU, memory, battery, network identity, sockets, and metric aggregates.
- **File integrity scan:** configurable local scan with progress, risk classification, and result details.
- **Event logs:** locally retained application events with level-based display and date filtering.
- **Radio monitor:** SDR hardware detection and spectrum/status information.
- **Settings:** application settings and appearance controls exposed by the current UI.

## Architecture

Darkworks Lab is built with modern reactive state management and modular services:

- `SecurityService` — perimeter scanning and device discovery.
- `NetworkSecurityService` — network host, port, and security checks.
- `SensorService` — hardware sensor streams.
- `SystemMonitorService` — system and performance telemetry.
- `FilesystemScannerService` — local file scanning.
- `RadioFrequencyService` — SDR detection and radio status.
- `LoggingService` and `DatabaseService` — local event and log persistence.
- `ThemeService` — light and dark themes and shared styling.

## Platform and permissions

Android declares internet, network-state, Wi-Fi-state, Bluetooth, location, notification, and storage-related permissions in its application manifest. Runtime location and Bluetooth permissions are requested on first launch on supported mobile platforms. Linux permission behavior depends on the host operating system and hardware configuration.

## Ownership

Copyright © 2026 Dark Work, LLC and darkworkllc@gmail.com. Proprietary software. All rights reserved.
