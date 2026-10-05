# Dumb Phone

Dumb Phone is a powerful network security and privacy application for Android. It leverages the native VPN Service API to provide deep packet inspection and filtering, allowing you to transform your smartphone into a secure, focused device.

**Package Name:** `com.dumbphone.dumbphone`

## Key Features

### 🛡️ Dual-Mode Protection
- **Dumb Phone Mode**: A strict "Default Block" policy. Only system-essential services (telephony, SMS) and user-whitelisted apps can access the network.
- **Soft Firewall Mode**: A "Default Allow" policy with intelligent filtering. It blocks traffic based on your custom rules and global threat intelligence.

### 🌍 Geo-Fencing & Blocklists
- **Continent-Based Protection**: Instantly block connections based on global regions: **North America (NA)**, **South America (SA)**, **Europe (EU)**, **Asia (AS)**, **Africa (AF)**, and **Oceania (OC)**. Includes pre-loaded data for over 100,000 IP ranges.
- **Lazy Loading & Parallel Sync**: IP ranges are downloaded in parallel and loaded asynchronously in the background, ensuring the UI remains responsive during updates.
- **Update Notifications**: Receive system alerts when threat intelligence data is successfully synchronized in the background.
- **Smart Refresh & Self-Healing**: Periodic recomputation of statistics from local logs ensures 100% data integrity, with a weekly update policy to minimize battery and data usage.
- **Custom Entries**: Add your own blocklist groups with manual IP or CIDR range entries, supported by the **P2P** blocklist.

### ⚙️ Granular Control
- **Custom Rules**: Create allow/block rules for specific IP addresses, ports, and protocols (TCP/UDP).
- **Live Monitoring**: Searchable connection logs with detailed metadata including destination, port, and responsible process. Logs are automatically grouped and summarized for clarity.

### 🎨 Modern Interface
- **Clean Design**: Beautiful, intuitive interface with smooth animations and Material Design 3 principles.
- **Dark Mode**: Full support for system-wide dark theme.
- **Elastic UI**: Fully responsive and optimized for all screen sizes, including support for phones and tablets. UI elements dynamically adapt to prevent overflows and layout issues.

## Privacy First
- **100% Local**: All filtering and logging occur entirely on your device.
- **No Data Export**: Your network activity never leaves the device.
- **Clean Slate**: Automatic database wipe on initial installation ensures a secure and optimized state for the grouped protection model.

## Legal Disclaimer
*This software is provided for educational and entertainment purposes only, "as is" with no guarantees, no warranty of any kind, and no liability for anything. Contact darkworkllc@gmail.com for support.*

## License
Proprietary — Copyright (c) 2026 Dark Work, LLC. All rights reserved.
