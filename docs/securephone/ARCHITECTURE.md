# Architecture — SecurePhone prototype

Status snapshot: **2026-09-17**, unreleased changes on package `securephone` version
`1.0.0+1`. Android debug packaging is verified; native device operation, secure
messaging and voice media are not validated. See [overview](./README.md) and
[security posture](./SECURITY.md).

## 1. Module Map

Source paths below are relative to `/home/bimo/workspace/securephone`.

| Module | Current responsibility |
|--------|------------------------|
| `lib/main.dart` | Material dashboard; owns services, starts Tor and waits for bootstrap, displays Tor/pin status; contact and PSTN buttons send REST requests, not media calls. Lifecycle detach requests Tor shutdown. |
| `lib/tor_service.dart` | Reuses a reachable SOCKS proxy; otherwise starts the embedded Android runtime or searches/spawns a desktop Tor binary. Records errors, probes SOCKS liveness, separately checks bootstrap, and stops owned runtimes. |
| `lib/tor_platform.dart` | Injectable `TorPlatform` interface and Android `securephone/tor` MethodChannel adapter. |
| `android/app/src/main/kotlin/com/example/securephone/TorPlatformHandler.kt` | Starts/binds tor-android, queries its SOCKS listener, unbinds/stops on explicit shutdown. Registered by `MainActivity`. |
| `lib/network_client.dart` | Singleton HTTP/raw TCP transport through SOCKS5, target host allow-list and IP-literal rejection. Forwards onion names as SOCKS domain requests rather than local DNS. TLS upgrade has a bad-certificate SPKI callback. |
| `lib/pinning.dart`, `lib/pin_provisioning_service.dart`, `lib/pin_startup.dart` | Pin models, DER/SPKI hashing, build configuration, signed provisioning payload checks and startup fallback. Defaults remain placeholders; see limitations below. |
| `lib/sms_service.dart` | `POST /send`, `GET /messages`, best-effort `GET /receipts` merged by ID, and `POST /receipts/ack`. Optional `SmsE2ee` hook; not enabled in the UI. |
| `lib/e2ee.dart` | Experimental custom DH/symmetric ratchet and identity bundle helpers. Not Signal/X3DH, unaudited, with no signed pre-keys or secure persistent sessions. |
| `lib/voip_service.dart` | REST initiation/PSTN requests plus unfinished WebRTC session and newline-delimited JSON socket signaling. ICE is socket-first with HTTP fallback, both via `NetworkClient`. |
| `test/`, `tool/tor_e2e_check.dart` | Unit/regression checks and opt-in live Tor connectivity checks; not Android native integration coverage. |

Dependencies include Flutter, `http`, `socks5_proxy`, `crypto`, `cryptography`,
`flutter_webrtc`, `path_provider` and `cupertino_icons`. Android Gradle pins
`info.guardianproject:tor-android:0.4.8.16` from Guardian Project Maven, with
transitive `jtorctl`. The APK includes Tor libraries for ARMv7, ARM64 and x86_64.

## 2. Runtime Sequences

- **Startup:** the dashboard starts Tor, checks SOCKS liveness, separately waits
  for bootstrap, and initializes pins. The badge distinguishes connecting from
  connected; pin provisioning failures retain build/baked-in configuration.
- **SMS:** the dialog calls `sendSms`, which posts recipient/message JSON through
  SOCKS. HTTP 200 means relay acceptance, not confirmed delivery. The UI does
  not provide an E2EE channel. Receipt fetching and acknowledgement are service
  APIs, not proof of an operational backend.
- **Calls:** contact/PSTN buttons send REST requests. They do not invoke
  `startWebRtcCall` or attach microphone tracks.
- **Draft socket signaling:** UTF-8 newline-delimited JSON with a `hello`
  message, SDP and ICE messages. This replaces the original `HELLO` example,
  but is not a complete interoperable signaling protocol.

## 3. State, Lifecycle & Errors

- UI state uses `setState`; network operations use futures and socket streams.
- SMS/REST operations generally return `false` or `[]` on errors. Tor startup
  records `lastError`/`spawnFailed`; its default startup timeout is 90 seconds
  and probe timeout is 5 seconds.
- Android startup rejects a reported SOCKS-port mismatch and cleans up failed
  starts. Embedded errors do not fall back to binary spawning. Explicit stop
  unbinds/stops the native service; Dart lifecycle detach requests shutdown.
  No native engine-detach handler or background keep-alive is implemented.
- `NetworkClient` is a singleton; changing proxy or pin settings rebuilds its
  HTTP client. No persistent per-peer encrypted session store exists.

## 4. Security Properties & Known Gaps

- Service HTTP/raw TCP requests use SOCKS, without a direct transport fallback.
  Onion names are passed to Tor rather than resolved through local DNS.
- Host allow-listing and IP-literal rejection exist. Endpoint flags do not
  update the fixed hosts in `PinBuildConfig`; custom relays require matching
  allow-list/provisioning integration. Defaults are placeholder services/pins.
- TLS SPKI checks run in a **bad-certificate callback**, not on every successful
  TLS connection. Normally trusted certificates can bypass that callback;
  do not claim universal pin enforcement. HTTP/raw signaling has no TLS pin
  check. See [security limitations](./SECURITY.md).
- The optional custom ratchet is not validated Signal/X3DH. Bundles are not
  signed, persistence is absent, and adversarial behavior is not validated.
  `fetchMessages` currently attempts decryption twice, discarding the first
  result; with stateful ratchets this can consume state and fail the second
  attempt. This is an outstanding code defect, not fixed by this doc update.
- WebRTC is relay-only with no TURN server, so media cannot connect. No local
  audio tracks or outgoing offer are created by the current session start.
  Message framing, duplicate dispatch and per-call routing still need work.
  Tor-backed signaling does not tunnel media through Tor.

## 5. Integration Work Remaining

1. Validate Android startup/bootstrap and stop/restart on a clean device
   without Orbot; packaging and mocked lifecycle tests are not device tests.
2. Deploy real onion SMS/signaling/PSTN backends and integrate matching host
   allow-lists, trust anchors and pin provisioning. URL constructors and
   `SECUREPHONE_*` endpoint flags alone are insufficient.
3. Replace the experimental crypto with a vetted protocol, authenticated
   per-peer sessions and secure persistence; fix and test SMS receive state.
4. Design a privacy-reviewed media path and complete signaling, microphone
   permissions/tracks, call lifecycle and UI integration.
5. Implement release signing, review native dependency security updates and
   third-party redistribution notices before distribution.

## 6. Verification & Platform Scope

Recorded verification on 2026-09-17: Android debug APK build succeeded, static
analysis was clean, and 47 tests passed with one opt-in live Tor test skipped.
Tor native libraries were inspected in the APK. No Android device or configured
emulator was available; native operation remains unverified. The Kotlin plugin
migration warning did not fail the build.

Desktop code searches for a local Tor binary. iOS has no Tor.framework binding;
its scaffold is not a self-contained Tor client. Other platform shells are not
validated, and the current `dart:io` networking is not a browser implementation.
