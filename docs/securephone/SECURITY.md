# Security Policy — SecurePhone

**Status — 2026-09-17:** unreleased prototype on main; package version
`1.0.0+1` is not a production security-support commitment. Do not use this
build for sensitive communications. See [project status](./README.md).

## 1. Threat Model (current)

Service HTTP/raw TCP requests use SOCKS5 without a direct transport fallback.
Onion names are forwarded to Tor rather than local DNS. These code properties
are not a security audit or proof of Android operation.

| Adversary | Intended protection | Remaining exposure |
|-----------|---------------------|--------------------|
| App server / onion operator | Tor-routed requests hide the client IP from the destination | Recipients, timing, call metadata and plaintext by default; experimental encryption is not a reliable security boundary |
| ISP / local network | Tor encrypts traffic between client and guard | Tor use is observable; traffic correlation remains possible |
| PSTN / SMS upstream | No end-to-end protection for ordinary telephone-network legs | Numbers, timing and plaintext legs; operational gateways are not included |
| Device thief / malware | No validated local-data protection | In-memory messages, no encrypted session store or app lock |

Tor-network attacks and endpoint compromise are not addressed by the client.
Malicious backends remain a risk. Do not represent SecurePhone as censorship-proof
or as a validated anonymous calling system.

### E2EE status

The custom ratchet in `/home/bimo/workspace/securephone/lib/e2ee.dart` is experimental, unaudited, and **not an implementation of Signal/X3DH**. Its pre-key bundles are not cryptographically signed. Passing basic round-trip tests does not establish protocol security, authenticated peer identity, replay safety, or safe state recovery after authentication failures. Do not use it to protect sensitive messages. It is opt-in through `SmsService(e2ee:)`; plaintext remains the default. Production E2EE requires a vetted protocol implementation, authenticated per-peer sessions, secure persistence, and adversarial testing.

### SMS and trust-configuration gaps

The dashboard does not attach an E2EE channel. `fetchMessages` currently attempts
decryption twice, discarding the first result; this can consume ratchet state
and break reception. Receipt APIs provide best-effort relay metadata, not
cryptographic delivery guarantees.

Endpoint overrides do not update the fixed host allow-list in `PinBuildConfig`.
Custom services need matching allow-list and trust configuration. Default hosts,
pins and provisioning configuration remain placeholders.

TLS SPKI checks run in a **bad-certificate callback**, not on every connection.
Normally trusted certificates can bypass that callback; universal pin enforcement
is not implemented. HTTP and raw socket signaling have no TLS pin check.
Provisioning failures retain build/baked-in configuration, which is not proof
of valid deployment trust.

## 2. Reporting a Vulnerability

- Contact maintainers through a confirmed private channel with `[SECURITY]` in
  the title. The configured repository is
  `http://mofo-jackson:6009/timotheuzi/SecurePhone`; do not assume its tracker is
  private or publicly accessible. Do not post sensitive details in public issues.
- Include the affected version/commit, reproduction steps, impact and redacted
  logs. Never include real phone numbers, message contents or private onion keys.
- Coordinate disclosure with maintainers. No dedicated security mailbox, PGP key
  or bug bounty is documented; this prototype does not establish a supported-release
  or response-time guarantee. Credit may be recorded in the
  [changelog](./CHANGELOG.md) with reporter consent.

## 3. Hardening Checklist (for release builds)

- [ ] Validate embedded Android Tor startup/bootstrap and stop/restart on-device.
- [ ] Configure real backends, matching allow-lists and authenticated provisioning.
- [ ] Enforce expected TLS pins on every relevant TLS connection and test bypass cases.
- [ ] Replace experimental crypto with a vetted protocol and secure session storage;
      fix SMS receive state handling and complete security review before enabling E2EE.
- [ ] Design and validate a media transport that meets the stated privacy goals.
- [ ] Review logging, permissions, platform lifecycle and background-service behavior.
- [ ] Configure production signing and reproducible builds; review dependency locks,
      upstream security updates and third-party notices before redistribution.

## 4. Known Limitations (unreleased prototype)

`isTorRunning` is a SOCKS5-handshake probe (liveness, not bootstrap proof — a freshly started daemon answers `05 00` before all circuits are built); `startTor` records startup failures in `lastError`. Android bundles tor-android 0.4.8.16 through the `securephone/tor` MethodChannel; other platforms still require a system/bundled binary. Explicit stop unbinds and stops the Android service. No background keep-alive or engine-detach shutdown is implemented. APK packaging has been verified, but native startup and bootstrap still require device validation. Review upstream Tor security updates before distribution.

WebRTC uses relay-only ICE with no configured TURN server, so the media draft cannot connect. Tor-backed signaling does not route WebRTC media through Tor; enabling direct candidates or ordinary TURN connections would introduce separate IP-exposure risks.

Recorded verification on 2026-09-17: successful Android debug APK build,
clean analysis, **47 tests passed and one live Tor test skipped**. Tor native
libraries were inspected for ARMv7, ARM64 and x86_64. No Android device or
configured emulator was available; mocked tests do not prove native operation.
Release builds still use debug signing keys. iOS has no Tor.framework binding;
other platform shells are unvalidated.

See [architecture](./ARCHITECTURE.md) for remaining integration work.
