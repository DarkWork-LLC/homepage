# Darkworks Lab — User Guide

**Package:** `com.darkworks.lab`
**Version:** 1.0.0+1
**Platforms:** Android and Linux

Darkworks Lab is a local-first application for learning, experimentation, and authorized defensive research. It inspects local devices, network activity, hardware telemetry, storage, and system health. It is not professional security advice and does not guarantee detection or protection. The developer assumes no responsibility or liability for any loss, damage, data loss, security incident, system change, or other consequence arising from use or inability to use the application. Use it only on systems and data you are authorized to inspect, and independently verify every result before taking action. Some features depend on device hardware, operating-system permissions, network access, and optional SDR equipment.

## Getting started

On the first Android launch the app requests location and Bluetooth-related permissions. Grant the permissions needed for the features you use. Use **Initialize perimeter** in the dashboard header, or pull down on the dashboard, to run the security service scan. Linux does not show the Android permission dialogs.

## Dashboard

The dashboard contains:

- **Status header:** shield artwork, active status, and the perimeter scan control.
- **Quick statistics:** Bluetooth and Network / Wi-Fi counts. The tiles remain side-by-side on narrow screens and open filtered device lists.
- **Network discovery:** up to four discovered network/Wi-Fi devices with an address summary.
- **Environment alerts:** the current dashboard displays a secure empty-state message.
- **Bottom navigation:** Status, Sensors, Security, System, and More.
- **Theme toggle:** the app-bar sun/moon button switches light and dark mode.

## Device lists

Tap either dashboard statistic to open **Device Discovery**. The list supports device-type filters, refresh, and the device details/actions currently implemented by the app. Results are local observations and may be limited by permissions, adapter state, and network reachability.

## Screens

### Sensors

The sensor monitor presents available accelerometer, gyroscope, magnetometer, ambient light, battery, and location data. Empty, unsupported, and permission-related states may appear depending on the host.

### Security

The Network Security screen provides scanner and log views. Scans can discover local hosts and inspect configured ports/services. Results are diagnostic observations, not a guarantee that a host is secure.

### System

System Monitor presents device information, CPU/memory/battery metrics, network identity, active sockets, and aggregate samples where the platform service can provide them.

### File Integrity Scan

The filesystem scanner walks accessible local files, reports progress, and classifies findings by risk. Results and any actions are limited to files and paths available to the application. Always review a result before deleting a file.

### Radio Spectrum Monitor

The radio screen reports SDR hardware availability and spectrum/status information. A compatible SDR and appropriate host support are required for useful results.

### System Event Logs

The logging screen shows local events with severity/level styling and date filtering available in the current implementation.

### Settings

System Settings exposes the settings available in the current build. Theme mode is also controlled from the dashboard.

## Privacy and safety

Monitoring data is handled by the application on the local device. This is educational software provided without a guarantee of complete detection or protection. Do not treat a clean result as proof that a device is secure.

## Troubleshooting

- **No Bluetooth results:** enable Bluetooth, grant scan/connect permissions, and refresh the scan.
- **No network results:** confirm the device is on the intended network and that local discovery is permitted.
- **Sensors unavailable:** check OS permissions, hardware support, and whether the stream is enabled.
- **Filesystem results are incomplete:** the scanner can only inspect paths exposed to the app; missing storage permissions reduce coverage.
- **No radio data:** connect a supported SDR and install the required host/runtime support.

## Ownership and liability

Contact **darkworkllc@gmail.com** for support. All rights reserved by **Dark Work, LLC**.
