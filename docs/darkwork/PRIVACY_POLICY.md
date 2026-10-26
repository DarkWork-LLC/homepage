# Privacy Policy

**Application:** Darkworks Lab
**Android package:** `com.darkworks.lab`
**Version:** 1.0.32
**Effective date:** October 25, 2026

## Educational use and limitation of responsibility

Darkwork Lab is provided for educational purposes, learning, experimentation, and authorized defensive research only. The developer assumes no responsibility or liability for any loss, damage, data loss, security incident, system change, or other consequence arising from use or inability to use this application. Users are responsible for legal authorization, backups, permissions, verifying results, and all decisions made from the output.

## Summary

Darkwork Lab is designed to perform its monitoring and analysis on the device where it is installed. The app does not operate a server for user data and does not intentionally transmit scan results, logs, sensor readings, filesystem results, or radio observations to Darkwork Lab.

Third-party Flutter packages and platform APIs can have their own behavior. The app’s current dependency list includes networking and device-access packages; users should review package licenses and platform disclosures before distribution.

## Information processed locally

Depending on permissions, hardware, platform, and the features used, the app may process:

- Bluetooth device identifiers, names, addresses, signal strength, and advertisements.
- Local network device names, addresses, interface details, host reachability, and open-port results.
- Sensor readings such as accelerometer, gyroscope, magnetometer, ambient light, location, and battery state.
- System telemetry such as device information, CPU, memory, battery, network interfaces, and sockets.
- File names, paths, metadata, and scanner findings from locations available to the app.
- SDR hardware status and radio-frequency observations when supported hardware is connected.
- Application events, settings, and locally persisted logs.

## How information is used

Information is used on-device to display monitoring status, perform scans, calculate local metrics, classify findings, and provide the user with reports and logs. Darkworks Lab does not use the information for advertising or an account-based service.

## Permissions

Android permissions are declared in `android/app/src/main/AndroidManifest.xml`. Following the Google Play Store "All Files Access" policy, the app does **not** request `MANAGE_EXTERNAL_STORAGE` (All Files Access). When the **File Integrity Scan** core setting is enabled, storage access is scoped to the MediaStore API via granular permissions:

- **Android 13+ (API 33+):** `READ_MEDIA_IMAGES`, `READ_MEDIA_VIDEO`, `READ_MEDIA_AUDIO` — requested at runtime only when the user initiates a scan.
- **Android < 33:** `READ_EXTERNAL_STORAGE` — requested at runtime only when the user initiates a scan.

Other runtime permissions include notifications (`POST_NOTIFICATIONS`), location, and Bluetooth (on the first launch on supported platforms). The app does not eagerly request any storage permission at startup; scanning is disabled by default and must be explicitly enabled in Settings.

The app does not require every permission for every feature. Granting a permission increases the data and device capabilities available to that feature. When file scanning is disabled, no storage permission is requested.

## Storage, sharing, and retention

Logs and scan data are stored or retained only as implemented by the relevant local service and platform storage. Data is not intentionally shared with third parties by the application. Uninstalling the app normally removes app-private data. The user remains responsible for backups, exported files, connected storage, and other copies outside the app sandbox.

The app does not provide a cloud account, cloud sync, or remote security-monitoring service. File scanning uses the MediaStore API on Android — it does not traverse the filesystem directly and does not access files outside MediaStore collections when enabled. When file scanning is disabled, no file contents or paths are accessed.

## User choices and deletion

Users can stop scans, disable streams where the UI exposes controls, clear or delete supported logs/results through the applicable screen, and uninstall the app to remove app-private data. Exported data must be removed by the user from the selected destination.

## Limitations

A clean scan is not a guarantee of privacy, security, or absence of threats. The app cannot inspect inaccessible files, unavailable sensors, unsupported devices, or networks that are outside its reach.

## Children

The app is not directed to children under 18. Do not use it to collect information about children.

## Contact and changes

Questions: darkworkllc@gmail.com

This policy may change as features and dependencies change. The current source and release documentation should be reviewed with each distribution.
