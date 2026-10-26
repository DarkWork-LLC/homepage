# Dumb Phone User Guide

Welcome to Dumb Phone! This guide helps you navigate the features of this network security application, designed to give you total control over your device's connectivity.

**Package Name:** `com.dumbphone.dumbphone`

## Table of Contents
1. [Introduction](#introduction)
2. [Dashboard](#dashboard)
3. [Firewall Modes](#firewall-modes)
4. [Custom Firewall Rules](#firewall-rules)
5. [Logs and Activity](#logs-and-activity)
6. [Country Blocklists](#blocklists)
7. [Settings](#settings)

## Documentation
- **[Google Play Guide](GOOGLE_PLAY_GUIDE.md)**: Instructions for publishing to Google Play Store.
- **[Privacy Policy](PRIVACY.MD)**: Complete privacy policy and data handling information.

---

## 1. Introduction <a id="introduction"></a>

Dumb Phone uses Android's VPN Service API to intercept and filter network traffic locally on your device. The app features a modern, beautiful, and **elastic interface** that adapts to any screen size with smooth animations and full dark mode support.

**Multi-Platform Support:**
- **Android**: Full support via native `VpnService` (Android 7.1+, API 25).
- **Linux**: Desktop builds run for development and testing (UI and local database via SQLite FFI). The firewall engine itself currently requires Android's `VpnService` — there is no iptables integration yet.

**Important:** You must grant **VPN Permission** when prompted for the firewall to function on Android. All processing is local; the app's only outbound network traffic is one-way downloads of public blocklist files (first launch and approximately weekly) — no personal or traffic data ever leaves the device.

## 2. Dashboard <a id="dashboard"></a>

The Dashboard is your control center with a clean, modern interface:
- **Status Cards**: Quickly toggle between Dumb Phone and Soft Firewall modes with beautifully designed cards showing real-time status.
- **Visual Indicators**: Status chips show **ACTIVE** (green) or **OFF** (red); a spinner with a progress bar appears while a mode is toggling.
- **Recent Counts**: Grouped log entries in the preview display repeat counts (e.g. `x5`) with red/green blocked/allowed icons.
- **Recent Activity**: A live preview of the latest network events with enhanced visual styling.

### Dashboard Features
- **Pull to Refresh**: Swipe down on the dashboard to refresh all statistics and data.
- **Mode Cards**: Each firewall mode has its own card with gradient icons, status indicators, and one-tap activation (tap the card to toggle).
- **Error Handling**: Beautiful error cards with clear messaging and easy dismissal.

## 3. Firewall Modes <a id="firewall-modes"></a>

### Dumb Phone Mode
The most restrictive state. It follows a "Block All" policy.
- **Behavior**: Blocks all outgoing traffic except for system-critical services.
- **Exceptions**: Phone calls and SMS are permitted.
- **Visual Style**: Orange-themed card with lock icon when active.
- **Best for**: Maximum privacy and focus.

### Soft Firewall
A balanced protection mode.
- **Behavior**: Allows traffic by default but filters it against your **Custom Rules** and **Country Blocklists**.
- **Visual Style**: Indigo-themed card with shield icon when active.
- **Best for**: Everyday use with enhanced security.

### Mode Management
- **Activation**: Tap a mode card to start that firewall mode.
- **Deactivation**: Tap the active card again to stop the mode.
- **Status Indicators**: 
  - 🟢 Green chip **ACTIVE**: mode is running
  - 🔴 Red chip **OFF**: mode is inactive
  - ⏳ Spinner: mode is toggling

## 4. Custom Firewall Rules <a id="firewall-rules"></a>

Define specific behavior for apps or servers. Both firewall modes evaluate rules stored locally on your device:
- **Rule Types**: 
    - **IP Address**: Target specific servers (e.g., `192.168.1.1`).
    - **Port / Protocol**: Enforce filtering per port and per protocol (TCP/UDP).
    - **Domain / Application**: Defined in the data model; enforcement is planned.
- **Actions**: Set to **Allow** (green) or **Block** (red).
- **Granularity**: You can specify Ports and Protocols (TCP/UDP) for IP rules.
- **Visual Design**: Rules display with color-coded action indicators, protocol chips, and smooth animations.

> **Current status:** Rules stored in the database are evaluated natively by both firewall modes (IP address, port, and protocol rules are enforced; domain/application rules are not yet enforced). The **Firewall Rules** management screen exists in the codebase but is **not yet wired into app navigation**, so rules cannot be created from the UI — this is planned for a future update.

### Managing Rules (screen pending navigation)
- **Add Rules**: Tap the "+" button to create new firewall rules.
- **Toggle Rules**: Use the switch on each rule card to enable/disable without deleting.
- **Delete Rules**: Tap the delete icon to remove a rule permanently.
- **Rule Details**: Each rule shows its type, target, port, protocol, and description.

## 5. Logs and Activity <a id="logs-and-activity"></a>

The **Logs** screen provides a transparent history of your device's networking with enhanced visual design:
- **Filtering**: Search for specific IP addresses or app names with the search bar.
- **Date Range**: View logs from specific days using the calendar date picker.
- **Visual Indicators**: 
  - Red badges for blocked connections
  - Green badges for allowed connections
- **Details**: Tap any log entry to see comprehensive details including source IP, destination port, protocol, and the process/package responsible.

### Log Features
- **Clear Logs**: Use the delete icon in the app bar to clear all logs (with confirmation dialog).
- **Refresh**: Tap the floating action button to refresh the log list.
- **Block Count**: See how many times a connection was blocked with the count badge.
- **Timestamps**: All logs show precise timestamps in HH:MM:SS format.

## 6. Country Blocklists <a id="blocklists"></a>

Prevent data exfiltration to specific regions or custom IP ranges with a modern, card-based interface:
- **Continent-Based Protection**: Countries are combined into logical groups based on global regions (**NA, SA, EU, AS, AF, OC**) to streamline management and improve performance.
- **Refresh**: Swipe down on the blocklist screen to refresh connection counts and synchronize data.
- **Sorting**: The list automatically sorts regions by the number of blocked connections (highest first).
- **Parallel Syncing**: The app uses **Parallel Downloads** and **Lazy Loading** for IP ranges. This ensures that large regional datasets are synchronized quickly and efficiently in the background.
- **Notifications**: You will receive a system notification once background updates are complete, keeping you informed of your device's security status.
- **Data Integrity**: A **Self-Healing** mechanism recomputes blocked connection statistics from local logs every few minutes to ensure accuracy.
- **Visual Design**: Icons display clear region acronyms (**NA, SA, EU, AS, AF, OC**) or **P2P** with gradient backgrounds and threat level badges.
- **Custom Entries**: Use the "+" floating action button to add your own blocklist entries with manual IP or CIDR ranges.
- **Details**: Tap any regional card to view a responsive list of included countries, specific IP ranges, and detailed threat metadata.

### Regional Categories
Categories are defined by geographical regions to provide intuitive control over global connectivity:
- 🌎 **North America (NA)**: Includes regions like US and Cuba.
- 🌎 **South America (SA)**: Includes regions like Venezuela.
- 🌍 **Europe (EU)**: Includes over 10 European nations and regional blocks.
- 🌏 **Asia (AS)**: Includes major Asian centers and strategic monitoring zones.
- 🌍 **Africa (AF)**: Includes African nations with specific monitoring requirements.
- 🌏 **Oceania (OC)**: Includes Australia, New Zealand, and surrounding regions.

### Blocklist Management
- **Toggle Countries**: Use the switch on each card to quickly enable/disable blocking for that country.
- **Search**: Use the search bar to filter countries by name or code.
- **Remove Entries**: In the details dialog, you can remove custom entries from the blocklist.

## 7. Settings <a id="settings"></a>

The Settings screen provides comprehensive control with a beautiful card-based layout:

### VPN Permission
- **Status Indicator**: Colored status card shows whether VPN permission is granted ("System access active") or awaiting authorization.
- **Grant Permission**: One-tap **ENABLE** button to request VPN access.

### Protection Zones
- **Continent Toggles**: Enable/disable blocking for each global region (North America, South America, Europe, Asia, Africa, Oceania) with color-coded switches.
- **Visual Feedback**: Toggle containers change color when active to provide clear visual feedback.
- **Reset Defaults**: Restore default threat intelligence settings.

### Log Retention
- **Adjustable Period**: Use the slider to set log retention from 1-30 days.
- **Visual Display**: Current retention period shown in a highlighted badge.
- **Range Indicator**: Clear text shows the valid range (1-30 days).

### Quick Actions
- **Clean Logs**: Delete all firewall logs immediately (a floating snackbar confirms "Logs purged").
- **Factory Reset**: Clear logs and rules, reset retention to its default, and rebuild blocklists from scratch (confirms with "Settings reset").
- **Visual Design**: Action buttons feature color-coded cards with rounded corners.

### Additional Settings
- **Floating Notifications**: Feedback messages use modern floating snackbars with rounded corners.

## Legal Disclaimer
This software is provided for educational and entertainment purposes only, "as is" with no guarantees, no warranty of any kind, and no liability for anything. Contact darkworkllc@gmail.com for support.

## Support
For issues, questions, or contributions, contact darkworkllc@gmail.com.
