# SecurePhone Software License

Copyright (c) 2026 SecurePhone Contributors. All rights reserved.

## Proprietary Software Notice

The SecurePhone application — including all source code, object code, binaries,
documentation, configuration, and associated materials in this repository
(collectively, the "Software") — is proprietary and confidential software of
SecurePhone Contributors.

Except for the rights expressly granted under the Third-Party Notices below,
**all right, title, and interest in and to the Software, including all
intellectual property rights, are and shall remain the exclusive property of
SecurePhone Contributors.**

Unless you have executed a separate written license agreement with SecurePhone
Contributors that covers the Software, the following applies: **you may not
use, copy, modify, create derivative works of, publicly display, perform,
distribute, sublicense, rent, lease, lend, or otherwise exploit the Software
(in whole or in part) without the prior written consent of SecurePhone
Contributors.**

Without limiting the foregoing, you must not:

- redistribute or otherwise transfer the Software (in source or binary form)
  to any third party without SecurePhone Contributors' prior written authorization;
- reverse engineer, decompile, disassemble, or attempt to derive the source code
  of the Software, except and only to the extent expressly permitted by
  applicable law notwithstanding this limitation;
- use the Software to develop or operate a competing product or service without
  SecurePhone Contributors' prior written consent;
- remove, alter, or obscure any proprietary notices on or in the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, AND TITLE. IN NO EVENT
SHALL SECUREPHONE CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
OF THE USE OF THE SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---

## Third-Party Notices

SecurePhone is built with Flutter/Dart and open-source packages. Each component is
used under its own license and is **not** covered by the proprietary notice
above; compliance with those licenses is the responsibility of the licensee.
Those licenses (and any required copyright notices) continue to apply to the
respective third-party code:

- Flutter SDK (BSD-3-Clause) — https://github.com/flutter/flutter
- `http`, `flutter_lints` (BSD-3-Clause, Dart team)
- `socks5_proxy` — see https://pub.dev/packages/socks5_proxy
- `path_provider` (BSD-3-Clause, Flutter team)
- `flutter_webrtc` (BSD-3-Clause) — https://github.com/flutter-webrtc/flutter-webrtc
- `cupertino_icons` (MIT)
- `crypto` and `cryptography` — see the licenses shipped with the resolved
  packages in the dependency lockfile.

### Bundled Tor runtime (status: 2026-09-17)

Android APKs now redistribute Tor native libraries through
`info.guardianproject:tor-android:0.4.8.16` from Guardian Project Maven, including
transitive `jtorctl`. Tor itself is separate software (3-clause BSD) —
https://www.torproject.org/. The Android wrapper, control client and native
transitive components retain their respective upstream licenses.
Desktop startup still uses a system or separately bundled Tor binary; iOS has
no embedded Tor.framework integration.

This list is an overview, not a complete redistribution-notice bundle. Before
shipping an APK, inventory all resolved Dart, Android and native dependencies,
preserve required upstream copyright/license texts, and satisfy their respective
redistribution obligations. Debug APK packaging verification does not establish
license compliance or production readiness. See [project status](./README.md).
These status notes do not change the proprietary terms above.

## Trademark Note

"Tor" and the onion logo are trademarks of The Tor Project, Inc. SecurePhone is an
independent project and is not affiliated with or endorsed by The Tor Project.
Use of these trademarks is for identification and attribution only.
