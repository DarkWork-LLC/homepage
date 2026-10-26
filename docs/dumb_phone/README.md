# Dumb Phone

Dumb Phone is a powerful network security and privacy application for Android. It leverages the native VPN Service API to provide deep packet inspection and filtering, allowing you to transform your smartphone into a secure, focused device.

**Package Name:** `com.dumbphone.dumbphone`

## Key Features

### 🛡️ Dual-Mode Protection
*   **Dumb Phone Mode**: A strict "Default Block" policy. Only system-essential services (telephony, SMS) and user-whitelisted apps can access the network.
*   **Soft Firewall Mode**: A "Default Allow" policy with intelligent filtering. It blocks traffic based on your custom rules and global threat intelligence.

### 🌍 Geo-Fencing & Blocklists
*   **Continent-Based Protection**: Instantly block connections based on global regions: **North America (NA)**, **South America (SA)**, **Europe (EU)**, **Asia (AS)**, **Africa (AF)**, and **Oceania (OC)**. Includes pre-loaded data for over 100,000 IP ranges.
*   **Lazy Loading & Parallel Sync**: IP ranges are downloaded in parallel and loaded asynchronously in the background, ensuring the UI remains responsive during updates.
*   **Update Notifications**: Receive system alerts when threat intelligence data is successfully synchronized in the background.
*   **Smart Refresh & Self-Healing**: Periodic recomputation of statistics from local logs ensures 100% data integrity, with a weekly update policy to minimize battery and data usage.
*   **Custom Entries**: Add your own blocklist groups with manual IP or CIDR range entries, supported by the **P2P** blocklist.

### ⚙️ Granular Control
*   **Custom Rules**: Create allow/block rules for specific IP addresses, ports, and protocols (TCP/UDP). The dedicated rules-management screen is not yet wired into navigation (planned) — see the User Guide for current status.
*   **Live Monitoring**: Searchable connection logs with detailed metadata including destination, port, and responsible process. Logs are automatically grouped and summarized for clarity.

### 🎨 Modern Interface
*   **Clean Design**: Beautiful, intuitive interface with smooth animations and Material Design 3 principles.
*   **Dark Mode**: Full support for system-wide dark theme.
*   **Elastic UI**: Fully responsive and optimized for all screen sizes, including support for Linux desktop, phones, and tablets. UI elements dynamically adapt to prevent overflows and layout issues.

## Privacy First
*   **100% Local**: All filtering and logging occur entirely on your device.
*   **No Data Export**: Your network activity never leaves the device.
*   **Clean Slate**: Automatic database wipe on initial installation ensures a secure and optimized state for the grouped protection model.
*   **Transparent Code**: Security logic implemented in Kotlin and Dart.

## Legal Disclaimer
This software is provided for educational and entertainment purposes only, "as is" with no guarantees, no warranty of any kind, and no liability for anything. Contact darkworkllc@gmail.com for support.

## Development
Use the provided `Makefile` for common tasks:
- `make android`: Build release APK.
- `make bundle`: Build AAB for Play Store.
- `make linux`: Build Linux desktop executable.
- `make dumbphone.zip`: Build debug APK with verbose logging.
- `make test`: Run unit tests.
- `make lint`: Run code analysis and linting.
- `make format`: Format code with dart format.
- `make container-start`: Start development environment in a container.

## Documentation
- **[User Guide](USER_GUIDE.md)**: Detailed usage instructions for all features.
- **[Google Play Guide](GOOGLE_PLAY_GUIDE.md)**: Step-by-step guide for publishing to Google Play Store.
- **[Privacy Policy](PRIVACY.MD)**: Complete privacy policy and data handling information.

## Tech Stack
- **Framework**: Flutter 3.47+
- **Language**: Dart 3.x, Kotlin 2.2+
- **Platform**: Android (API 25–36) & Linux
- **Build System**: Gradle 9.4.1, AGP 8.13.0
- **Architecture**: MVVM with ViewModel pattern
- **State Management**: ValueListenable-based reactive state
- **Database**: SQLite (sqflite) with FFI support for Desktop

## Building from Source

### Prerequisites
- Flutter SDK (3.24.0 or higher)
- Android SDK
- JDK 17+

### Quick Start
```bash
# Install dependencies
flutter pub get

# Run linter
make lint

# Run tests
make test

# Build release APK
make android

# Build release bundle for Play Store
make bundle
```

## License
Proprietary — Copyright (c) 2026 Dark Work, LLC. All rights reserved. See [LICENSE](LICENSE) for the full terms.
