# SecurePhone

SecurePhone is a communications prototype with Tor-backed SMS relay requests
and call signaling. Tor hides the client's IP from those destination services;
it does not hide recipients, timing, or other metadata from the relay.
End-to-end encryption and voice media are not production-ready (see below).

> **Proprietary and confidential.** SecurePhone is proprietary software of
> SecurePhone Contributors. **All rights reserved.** Use of this software is
> governed by the terms set forth in [`LICENSE.md`](./LICENSE.md); nothing in
> this repository grants you a license to copy, modify, distribute, or
> otherwise exploit SecurePhone except as expressly stated in that license.

## Project status — 2026-09-17

This is an unreleased prototype; the package version remains `1.0.0+1`
(package name `securephone`). The most recent verification recorded a successful
Android debug APK build, clean static analysis, and **47 passing tests with
one live Tor test skipped**. Tor native libraries were verified in the APK
for ARMv7, ARM64 and x86_64. No Android device or configured emulator was
available, so native startup/bootstrap and stop/restart remain unverified.
The `flutter_webrtc` Kotlin Gradle Plugin warning did not fail that build;
compatibility with future Flutter versions still needs attention.

The dashboard sends relay requests, not completed voice calls. It does not
attach the experimental encryption channel. There are no working backends
included, no production signing setup, and no validated secure-messaging release.
See [architecture](./ARCHITECTURE.md) and [security limitations](./SECURITY.md).


## Features

- **Tor-backed requests** — SMS relay requests and call signaling use
  `NetworkClient` through a local SOCKS5 proxy, without a direct fallback.
- **Embedded Tor on Android** — the APK includes `tor-android` 0.4.8.16 and
  its native libraries; no separate Orbot installation or runtime download
  is required. Non-Android platforms still require a Tor binary.
- **Configurable relays** — SMS, VoIP and PSTN endpoints are configurable.
  The default onion names are placeholders, not working services.
- **Experimental messaging/media** — SMS encryption is opt-in and unaudited.
  The WebRTC draft uses relay-only ICE with no TURN server, so media cannot
  connect. Tor signaling alone does not tunnel WebRTC media.

## Android build and verification

From `/home/bimo/workspace/securephone`, run `flutter build apk --debug`.
The artifact is
`/home/bimo/workspace/securephone/build/app/outputs/flutter-apk/app-debug.apk`.
The minimum Android API level is at least 24. Release signing is still configured
with debug keys; do not distribute that as a production release.

Configure your own services with `SECUREPHONE_SMS_ONION`,
`SECUREPHONE_VOIP_ONION`, `SECUREPHONE_PSTN_ONION`, and
`SECUREPHONE_VOIP_SIGNALING_HOST` / `SECUREPHONE_VOIP_SIGNALING_PORT`
using `--dart-define`. These overrides do **not** update the host allow-list:
`PinBuildConfig` still uses fixed placeholder hostnames. Integrate matching
host entries via `NetworkClient.setPinnedServices` or revise the build/provisioning
configuration before using custom services; endpoint flags alone are insufficient.
The default pins and provisioning host are placeholders, not deployable trust
configuration. See [security limitations](./SECURITY.md) before relying on TLS pins.
Bundling Tor makes the client runtime self-contained, not the relay backends.

Android startup uses the embedded service and checks its reported port against
9050 before the usual SOCKS5 probe. Startup errors trigger service cleanup;
there is no binary-spawn fallback after an embedded-runtime error.
`isTorRunning()` proves SOCKS liveness, not a built Tor circuit; the app uses
`waitForBootstrap()` separately.

Unit tests and APK packaging do not prove native startup. Device validation is
still required: install on a clean Android device without Orbot, launch, wait
for bootstrap, test a configured onion request, and verify stop/restart.
Background keep-alive is not implemented.

## Third-Party Software

SecurePhone depends on open-source components (Flutter SDK, `http`,
`socks5_proxy`, `path_provider`, `flutter_webrtc`, `cupertino_icons`, and Tor
itself). These are used under their own licenses and are **not** covered by
SecurePhone's proprietary license — see [`LICENSE.md`](./LICENSE.md)
(Third-Party Notices). Android APKs redistribute Tor through the pinned
`info.guardianproject:tor-android:0.4.8.16` AAR (including transitive `jtorctl`).
On desktop, `TorService` spawns a local system or bundled Tor binary. Review
upstream licenses and security updates before distribution.

## Legal

- SecurePhone is **not** affiliated with or endorsed by The Tor Project.
- "Tor" and the onion logo are trademarks of The Tor Project, Inc.
- See [`SECURITY.md`](./SECURITY.md) for the security posture and accepted
  limitations of the current release.

