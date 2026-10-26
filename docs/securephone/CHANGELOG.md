# Changelog — SecurePhone

All notable changes tracked in Keep-a-Changelog format. Versioning: `pubspec.yaml` (`major.minor.patch+build`).

## [Unreleased]

### Status — 2026-09-17

Package version remains `securephone` `1.0.0+1`; these changes are a prototype,
not a production release. Recorded verification: successful debug APK build,
clean analysis, **47 tests passed and one live Tor test skipped**. Tor libraries
were inspected for ARMv7, ARM64 and x86_64. Android native startup/bootstrap and
stop/restart remain unverified: no device or configured emulator was available.
The Kotlin migration warning did not fail the build. Release signing still
uses debug keys; iOS has no Tor.framework binding.

Known gaps: endpoint flags do not update the host allow-list; default services
and pins are placeholders. TLS SPKI checks use a bad-certificate callback,
not every TLS connection. SMS receive currently attempts decryption twice,
which can consume ratchet state. E2EE is not enabled in the dashboard, and
voice media is unfinished. See [security limitations](./SECURITY.md).

### Added

- **Embedded Tor (tor-android)**: `info.guardianproject:tor-android` + `jtorctl` bundled into the APK (Guardian Project Maven repo in `settings.gradle.kts`). `TorPlatformHandler.kt` binds `org.torproject.jni.TorService`, starts/stops it via the new `securephone/tor` MethodChannel and reports the SOCKS port from the control connection (`net/listeners/socks`). `TorService.startTor` prefers the embedded runtime and falls back to spawning a system/bundled binary elsewhere; the `isTorRunning` SOCKS5-handshake probe contract is unchanged. Android manifest gains the `TorService` declaration, `FOREGROUND_SERVICE`(+special-use) and `POST_NOTIFICATIONS` permissions; `minSdk` floored at 24.
- **Experimental crypto**: custom X25519/HKDF-SHA256/ChaCha20-Poly1305 ratchet helpers and basic round-trip/out-of-order tests. This is **not Signal/X3DH**; bundles are unsigned and authenticated per-peer persistence and adversarial validation are missing.
- **SMS E2EE + receipts**: `SmsService` gains an optional `e2ee` layer — `sendSms` encrypts the body into a ratchet envelope before JSON-encode; `fetchMessages` decrypts envelopes, marks `e2ee` per message, merges `/receipts` into each message as `receipt` and adds `ackMessageReceipt`.
- **Self-hosted onions**: default SMS/VoIP/PSTN/signaling endpoints overridable at build time via `--dart-define` (`SECUREPHONE_SMS_ONION`, `SECUREPHONE_VOIP_ONION`, `SECUREPHONE_PSTN_ONION`, `SECUREPHONE_VOIP_SIGNALING_HOST/PORT`).
- **WebRTC draft**: peer-connection and socket-signaling scaffolding, socket-first ICE with HTTP fallback, and teardown APIs. Relay-only ICE is configured with no TURN server, so media cannot connect. Session startup does not create an outgoing offer or attach local audio; the dashboard only sends REST call requests. Tor signaling does not tunnel media.

### Fixed

- Tor transport/startup improvements (the current live test is opt-in and was skipped; these changes are not Android end-to-end verification):
  - `TorService` now finds bundled Tor installations (Tor expert bundle under `~/.local/share/securephone/tor/` or `$XDG_DATA_HOME/securephone/tor/`, Tor Browser layout, system paths), injecting `LD_LIBRARY_PATH` for the bundle's private libevent/libssl and using a dedicated writable `--DataDirectory` so it never collides with a system daemon's `~/.tor` lock.
  - Added `waitForBootstrap()`: the SOCKS port accepts connections before Tor finishes bootstrapping, so early requests fail with SOCKS `serverError`. The app now waits until a real circuit is built (probe: payload-less SOCKS5 CONNECT to the Tor Project's onion) before declaring "Tor: connected"; the badge shows "Tor: connecting…" meanwhile, and pin initialization runs only after bootstrap.
  - Daemon exiting during startup (bad flags, port conflict, unwritable directory) now fails fast with `Tor daemon exited during startup (exit code N)` instead of stalling until timeout.
- Tor never connected in practice:
  - `NetworkClient` routed onion requests through `socks5_proxy` with `InternetAddress(host)`, which throws for non-DNS-resolvable `.onion` names (`Invalid internet address '…'`) — every Tor-routed request failed before reaching the proxy. Onion hostnames are now forwarded verbatim as SOCKS5 domain requests (and IP-literal targets are rejected outright to prevent clearnet leaks).
  - `isTorRunning` used a bare TCP connect with a 1 s timeout, probed immediately after `Process.start` (before Tor had bound its listener), and gave false positives for any TCP squatter. It now performs a real SOCKS5 greeting handshake; `startTor` polls up to 90 s.
  - `startTor` swallowed spawn errors (missing `tor` binary on desktop, no binary on Android at all). Failures now surface via `lastError`/`spawnFailed`, the dashboard shows the reason, and the refresh FAB re-attempts startup (also picking up an externally running daemon, e.g. a system tor or Orbot).
  - Tor's stdout/stderr pipes were never drained (daemon could stall on a full pipe) and `stopTor` leaked an unknown-state process; both handled now.
  - HTTPS-over-SOCKS pinned-cert callback was never wired into the TLS upgrade; pinning now runs inside the SOCKS connection builder.
  - Pin provisioning failures other than `PinValidationException` (e.g. TLS/handshake errors while pins were still placeholders) escaped `initializePinning`; all failures now degrade to the baked-in allow-list as documented.

- Android lifecycle cleanup now unbinds/stops the owned service, rejects a reported SOCKS-port mismatch, and cleans up failed starts without binary-spawn fallback. Mocked lifecycle tests cover startup, cleanup and restart; native behavior remains unverified.
- Updated all six project Markdown files to distinguish verified packaging from unverified operation and unfinished security/media features; preserved proprietary license terms and corrected bundled-Tor notices.

## [1.0.0] — 2026-09-15 (initial scaffold, not a validated release)

### Added

- Flutter scaffold (`securephone` 1.0.0+1, Dart ^3.13.3) with Android/iOS/Linux/macOS/Windows/Web shells.
- `TorService`: spawn `tor --SocksPort`, 1 s SOCKS liveness probe, `stopTor`, `proxyAddress`.
- `NetworkClient` singleton: SOCKS5-routed `IOClient` (`socks5_proxy` + `http`/`io_client`) + raw `connectSocket` for signaling; test-injectable client.
- `SmsService`: `POST /send` + `GET /messages` against `tor-sms-service.onion` (JSON over Tor).
- `VoipService`: `initiateCall` via `{_signalingUrl}/call/initiate` (POST JSON, `200 == success`, swallow → false), `callPstn` via `tor-pstn-gateway.onion/dial`, `sendIceCandidate` + `connectToSignalingSocket` (`tor-voip-signaling.onion:8080`).
- `MainScreen` dashboard: Tor badge, secure contacts + one-tap call, PSTN dialer, Secure SMS dialog, refresh FAB, `AppLifecycleListener.onDetach → stopTor`.
- Tests: `tor_service`, `network_client`, `sms_service` (MockClient), `voip_service` suites.

### Dependencies

- `cupertino_icons ^1.0.8`, `socks5_proxy ^2.1.1`, `http ^1.6.0`, `path_provider ^2.1.6`, `flutter_webrtc ^1.6.2+hotfix.2`; dev `flutter_lints ^6.0.0`, `flutter_test`.
