# User Guide — online_snesgems_emulator

A Python-Django web application that runs Super Nintendo (SNES) games
directly in your web browser, plus a Django WYSIWYG rich-text page editor.

## Contents

1. [Overview](#overview)
2. [System requirements](#system-requirements)
3. [First launch](#first-launch)
4. [Playing a game](#playing-a-game)
5. [Controls](#controls)
6. [Button configuration (key remapping)](#button-configuration)
7. [Save states](#save-states)
8. [Settings menu](#settings-menu)
9. [Audio](#audio)
10. [WYSIWYG page editor](#wysiwyg-page-editor)
11. [Django admin](#django-admin)
12. [Deployment on PythonAnywhere](#deployment-on-pythonanywhere)
13. [Troubleshooting](#troubleshooting)

---

## 1. Overview

The emulator runs **client-side in your browser** (Snes9x compiled to
WebAssembly). The Django backend only serves the user interface, the ROM
library metadata, and the binary ROM streams; the emulation itself happens
locally, so there is no server-side lag during play.

The app also includes a WYSIWYG rich-text page editor at `/wysiwyg/` for
authoring HTML pages backed by SQLite.

---

## 2. System requirements

- A modern desktop or mobile browser with WebAssembly and IndexedDB support
  (Chrome, Edge, Firefox, Safari).
- A **secure context** for save states: `https://` in production, or
  `http://localhost` when running locally (`localhost` counts as secure).
- Python 3.10+ and Django 5.0+ to run the backend (see Setup below).

---

## 3. First launch

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create the database tables
python manage.py migrate

# 3. Register the bundled ROMs
python manage.py seed_roms

# 4. Start the development server
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

A `Makefile` is also provided for common tasks:

```bash
make setup    # venv, dependencies, migrate, seed ROMs, collectstatic
make run      # run the dev server
make test     # run the Playwright end-to-end smoke test
```

See `README.md` for the full setup/run instructions.

---

## 4. Playing a game

1. Open `http://127.0.0.1:8000/`. The ROM library lists the bundled games.
2. Click a game card (or select it from the dropdown) to load it.
3. Press **Play** to start emulation. The game renders to the canvas.
4. Use **Pause** to suspend and **Reset** to restart the game.

Ten games are bundled, including *Chrono Trigger*, *Final Fantasy III*,
*Blackthorne*, *Metal Marines*, and others (see `README.md` for the full list).

ROM data is streamed from `GET /api/roms/<id>/stream/` and handed to the
WebAssembly emulator in your browser.

---

## 5. Controls

### Keyboard

| SNES button | Default key |
|-------------|-------------|
| D-pad Up | Arrow Up |
| D-pad Down | Arrow Down |
| D-pad Left | Arrow Left |
| D-pad Right | Arrow Right |
| A | X (configurable) |
| B | Z / C |
| X / Y | Action diamond keys |
| L / R | Shoulder keys |
| Start | Start key |
| Select | Select key |

The exact default mapping follows the SNES diamond layout and can be
reassigned (see section 6).

### USB gamepads

USB gamepads are polled automatically and work on desktop browsers with no
configuration.

### On-screen virtual gamepad (touch, mouse, trackpad)

On phones, tablets, and trackpads, use the on-screen virtual gamepad:

- **D-pad** — directional input
- **Shoulder buttons** — L, R
- **Action diamond** — X, Y, A, B
- **Start / Select** — system buttons
- **Thumbstick** — draggable analog directional input

Buttons flash with a blue glow when tapped or clicked. The virtual gamepad
supports touch, mouse, and trackpad input.

---

## 6. Button configuration

You can reassign key bindings for all 12 controller buttons. New bindings are
saved to your browser's `localStorage` and persist across sessions.

Open the button configuration screen in the emulator UI, press a controller
button, then press the key you want to bind to it. Bindings are applied
immediately and stored locally.

---

## 7. Save states

Save states are snapshots of the emulator's memory, stored in your browser's
IndexedDB (no server round-trip).

- **Save:** give the state a name and confirm — it is stored locally.
- **Load:** choose a saved state from the list and load it to resume exactly
  where you left off.
- **Delete:** remove a saved state you no longer need.
- **Download:** export a save state as a `.sav` file to your computer.

Save states are private to your browser and device; they are not synced or
uploaded.

---

## 8. Settings menu

Press **Escape** during a game to open the in-game settings menu. You can
adjust:

- Region (NTSC / PAL)
- Aspect ratio
- Render filter
- Volume (and Mute)
- Interpolation
- Sprite limit
- Other emulator options

Changes take effect immediately.

---

## 9. Audio

Audio uses the Web Audio API. Because browsers block audio until you interact
with the page, the app performs an **autoplay policy unlock** on first
interaction. Use the **Mute** toggle to silence audio at any time.

---

## 10. WYSIWYG page editor

The editor at `/wysiwyg/` lets you create, edit, preview, and delete rich-text
pages using native browser content editing (no build step, no external CDN).

| Path | What it does |
|------|--------------|
| `/wysiwyg/` | Page list — view all pages |
| `/wysiwyg/new/` | Create a new page |
| `/wysiwyg/<slug>/edit/` | Edit an existing page |
| `/wysiwyg/<slug>/` | Public read-only view of a page |
| `/wysiwyg/api/save/` | Save page content (POST JSON) |
| `/wysiwyg/api/delete/` | Delete a page (POST JSON) |
| `/admin/` | Django admin — manage Pages |

### Writing a page

1. Go to `/wysiwyg/new/`.
2. Enter a title and format the content with the rich-text toolbar.
3. Save — a URL slug is generated automatically from the title.
4. View your published page at its public URL, or edit it later.

Page content is stored in SQLite and can also be managed through the Django
admin (`/admin/`).

---

## 11. Django admin

Log in as a superuser at `/admin/` to:

- Manage ROM records (add/remove games from the library)
- Manage WYSIWYG pages
- Manage site users

Create a superuser with:

```bash
python manage.py createsuperuser
```

---

## 12. Deployment on PythonAnywhere

Full PythonAnywhere-specific deployment steps are in `README_PYTHONANYWHERE.md`.
The short version:

1. Upload the project to your PythonAnywhere account.
2. Create a **Manual configuration** web app pointing WSGI at the root-level
   `wsgi.py`.
3. Map static files: URL `/static/`, directory
   `/home/<username>/online_snesgems_emulator/staticfiles`.
4. In a bash console:
   ```bash
   pip install Django>=5.0
   python manage.py migrate
   python manage.py seed_roms
   python manage.py collectstatic --noinput
   ```
5. Reload the web app and visit your domain.

Re-run `collectstatic` whenever you change CSS, JS, or vendor files.

---

## 13. Troubleshooting

| Problem | Likely cause / fix |
|---------|-------------------|
| ROM list doesn't load | Make sure the Django dev server is running (`python manage.py runserver`). |
| Static files blocked (MIME `text/html`) | On PythonAnywhere, run `collectstatic` and map `/static/` to `staticfiles/`, not `static/`. |
| Save states unavailable | Open the site over HTTPS or `localhost`. IndexedDB/OPFS require a secure context. |
| Audio doesn't play | Interact with the page first (browsers block autoplay), then unmute. |
| Buttons don't respond | Reassign bindings in the button configuration screen, or check your USB gamepad. |

---

## License & related documents

- `LICENSE` — MIT License (open source)
- `PRIVACY.md` — Privacy policy
- `README.md` — Project overview and setup
- `README_PYTHONANYWHERE.md` — PythonAnywhere deployment guide

Bundled ROMs are provided for personal/backup use only; comply with applicable
copyright law in your jurisdiction.
