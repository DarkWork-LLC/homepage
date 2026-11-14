# Privacy Policy

**Effective date:** November 14, 2026  
**Project:** online_snesgems_emulator — a Django web application that emulates
Super Nintendo (SNES) games in the browser and includes a WYSIWYG page editor.

This privacy policy explains what information is collected, how it is stored,
and who can access it when you use this application.

---

## 1. No personal accounts or tracking

The application does **not** require you to create an account, does **not**
collect your name, email address, or any other personally identifiable
information, and does **not** run analytics, advertising, or tracking scripts.
There are no third-party services, no external CDNs, and no social-media
widgets integrated into the app.

---

## 2. Data that stays on your device (client-side)

The SNES emulator runs entirely in your web browser (Snes9x compiled to
WebAssembly). The following data is stored **only in your browser** and is
never sent to the server:

| Data | Where it is stored | Purpose |
|------|-------------------|---------|
| Save states | IndexedDB (database `snes-emu`, store `save-states`) | Save and reload in-game progress |
| Cartridge SRAM / battery-backed saves | Origin Private File System (OPFS) | Persist game saves across sessions |
| Button / key bindings | `localStorage` | Remember your controller remapping |
| Audio mute preference | `localStorage` / in-memory config | Remember volume/mute state |
| Emulator settings (region, filter, aspect, etc.) | In-memory only (current session) | Your play preferences |

You can delete this data at any time by clearing your browser's site data
(cookies, local storage, IndexedDB, and file system storage) for the site, or
by using the in-app delete controls for individual save states.

---

## 3. Data stored on the server (Django backend)

The Django backend stores the following in a SQLite database (`db.sqlite3`)
on the server where the app is hosted:

- **ROM library metadata:** display name, filename, and file size of each
  bundled Super Nintendo ROM. The ROM binaries themselves live on disk under
  `roms/` and are streamed to your browser on demand so the emulator can run
  them.
- **WYSIWYG pages:** title, slug, and rich-text HTML content that *you*
  author through the page editor at `/wysiwyg/`. This content is provided by
  you and can be edited or deleted at any time.
- **Django admin users:** if a superuser is created for administration, the
  username and hashed password are stored by Django's auth system.

---

## 4. Cookies

The Django backend uses standard session and CSRF cookies:

- `sessionid` — maintains your authenticated session if you log in to the
  Django admin (`/admin/`). Not used by the emulator or public pages.
- `csrftoken` — protects the WYSIWYG save/delete API endpoints against
  cross-site request forgery. Read automatically by the editor frontend.

Both cookies are set as secure in production (HTTPS only). No tracking or
third-party cookies are used.

---

## 5. Server logs

The hosting platform (e.g. PythonAnywhere) may keep standard HTTP access logs
(IP address, requested path, status code, user agent) for the operation and
security of the service. This project itself does not process or analyze
those logs. If you self-host, you control your own server logs.

---

## 6. Data retention and deletion

- **Client-side data:** persists until you clear your browser's site data or
  delete individual save states in the emulator.
- **WYSIWYG pages:** persist in SQLite until you delete them through the
  editor API (`/wysiwyg/api/delete/`) or the Django admin.
- **To delete all your data:** clear your browser's site data for the domain
  (removes save states, SRAM, key bindings) and delete your WYSIWYG pages via
  the editor or admin interface. If you need the server database removed,
  contact the instance operator.

---

## 7. Security

- The emulator and WYSIWYG editor require a secure context (HTTPS or
  `localhost`) because IndexedDB and OPFS are restricted to secure origins.
- In production, session and CSRF cookies are marked `Secure`, and the app
  relies on HTTPS termination at the hosting layer.
- ROM files are served as `application/octet-stream` streams; no user
  uploads are accepted.

---

## 8. Children

The application does not knowingly collect personal information from anyone.
Because no personal information is collected at all, there is nothing specific
to children to protect beyond the general practices above.

---

## 9. Changes to this policy

This policy may be updated from time to time. The current version is kept in
the repository at `PRIVACY.md`.

---

## 10. Contact

If you have questions about this privacy policy or about your data, contact
the repository maintainer via the GitHub issue tracker:

https://github.com/DarkWork-LLC/online_snesgems_emulator
