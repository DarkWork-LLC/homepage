# Dumb Phone User Guide

Welcome to Dumb Phone! This guide helps you navigate the features of this network security application, designed to give you total control over your device's connectivity.

**Package Name:** `com.dumbphone.dumbphone`

## Table of Contents
1. [Introduction](#1-introduction)
2. [Dashboard](#2-dashboard)
3. [Firewall Modes](#3-firewall-modes)
4. [Custom Firewall Rules](#4-custom-firewall-rules)
5. [Logs and Activity](#5-logs-and-activity)
6. [Country Blocklists](#6-country-blocklists)
7. [Settings](#7-settings)

---

## 1. Introduction
Dumb Phone uses Android's VPN Service API to intercept and filter network traffic locally on your device. The app features a modern, beautiful, and **elastic interface** that adapts to any screen size with smooth animations and full dark mode support.

**Important:** You must grant **VPN Permission** when prompted for the firewall to function on Android. All processing is local; the app's only outbound network traffic is one-way downloads of public blocklist files (first launch and approximately weekly) — no personal or traffic data ever leaves the device.

## 2. Dashboard
The Dashboard is your control center with a clean, modern interface:
- **Status Cards**: Quickly toggle between Dumb Phone and Soft Firewall modes with beautifully designed cards showing real-time status.
- **Visual Indicators**: Status chips show **ACTIVE** (green) or **OFF** (red); a spinner with a progress bar appears while a mode is toggling.
- **Recent Counts**: Grouped log entries in the preview display repeat counts (e.g. `x5`) with red/green blocked/allowed icons.
- **Recent Activity**: A live preview of the latest network events with enhanced visual styling.

### Dashboard Features
- **Pull to Refresh**: Swipe down on the dashboard to refresh all statistics and data.
- **Mode Cards**: Each firewall mode has its own card with gradient icons, status indicators, and one-tap activation (tap the card to toggle).
- **Error Handling**: Beautiful error cards with clear messaging and easy dismissal.

## 3. Firewall Modes

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

## 4. Custom Firewall Rules
Define specific behavior for apps or servers. Both firewall modes evaluate rules stored locally on your device:
- **Rule Types**:
  - **IP Address**: Target specific servers (e.g., `192.168.1.1`).
  - **Port / Protocol**: Enforce filtering per port and per protocol (TCP/UDP).
- **Actions**: Set to **Allow** (green) or **Block** (red).
- **Granularity**: You can specify Ports and Protocols (TCP/UDP) for IP rules.
- **Visual Design**: Rules display with color-coded action indicators, protocol chips, and smooth animations.

## 5. Logs and Activity
The **Logs** screen provides a transparent history of your device's networking with enhanced visual design:
- **Filtering**: Search for specific IP addresses or app names with the search bar.
- **Date Range**: View logs from specific days using the calendar date picker.
- **Visual Indicators**: Red badges for blocked connections, Green badges for allowed connections.
- **Details**: Tap any log entry to see comprehensive details including source IP, destination port, protocol, and the process/package responsible.

## 6. Country Blocklists
Prevent data exfiltration to specific regions or custom IP ranges with a modern, card-based interface:
- **Continent-Based Protection**: Countries are combined into logical groups based on global regions (**NA, SA, EU, AS, AF, OC**) to streamline management and improve performance.
- **Refresh**: Swipe down on the blocklist screen to refresh connection counts and synchronize data.
- **Sorting**: The list automatically sorts regions by the number of blocked connections (highest first).
- **Parallel Syncing**: The app uses **Parallel Downloads** and **Lazy Loading** for IP ranges.
- **Notifications**: You will receive a system notification once background updates are complete.
- **Data Integrity**: A **Self-Healing** mechanism recomputes blocked connection statistics from local logs every few minutes.
- **Visual Design**: Icons display clear region acronyms (**NA, SA, EU, AS, AF, OC**) or **P2P** with gradient backgrounds.
- **Custom Entries**: Add your own blocklist entries with manual IP or CIDR ranges.

## 7. Settings
The Settings screen provides comprehensive control with a beautiful card-based layout:

### VPN Permission
- **Status Indicator**: Colored status card shows whether VPN permission is granted ("System access active") or awaiting authorization.
- **Grant Permission**: One-tap **ENABLE** button to request VPN access.

### Protection Zones
- **Continent Toggles**: Enable/disable blocking for each global region (North America, South America, Europe, Asia, Africa, Oceania) with color-coded switches.
- **Reset Defaults**: Restore default threat intelligence settings.

### Log Retention
- **Adjustable Period**: Use the slider to set log retention from 1-30 days.

### Quick Actions
- **Clean Logs**: Delete all firewall logs immediately.
- **Factory Reset**: Clear logs and rules, reset retention to default, and rebuild blocklists from scratch.

## Legal Disclaimer
*This software is provided for educational and entertainment purposes only, "as is" with no guarantees, no warranty of any kind, and no liability for anything. Contact darkworkllc@gmail.com for support.*

## Support
For issues or questions, contact darkworkllc@gmail.com.
