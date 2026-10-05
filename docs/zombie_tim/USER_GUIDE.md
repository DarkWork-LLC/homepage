# 🧟 Zombie Tim - User Guide 🧟

Welcome to the official user guide for **Zombie Tim**, your favorite undead AI assistant! This guide will help you navigate the gory details of interacting with Tim and making the most of his decaying brain.

---

## 🚀 Getting Started

When you first open the app, you'll be greeted by **Zombie Tim** himself. He might be a bit twitchy, but he's friendly (mostly)!

1.  **Launch the App**: Open Zombie Tim on your Android, iOS, Web, Linux, Windows, or macOS device.
2.  **Initialize**: On first run, Tim sets up his "Brain Database" (SQLite) to remember your interactions.
3.  **Start Chatting**: Use the bottom navigation to jump between screens. The Chat header always reminds you: type **`help`** to see every command Tim knows.

> 💡 **Lost?** Type **`help`** (or **`what can you do`**) at any time.

---

## 📱 Main Interface

The app has three main screens accessible via the bottom navigation bar:
1. **Chat (💬)**: The main interface for talking to Tim. Interact with Tim's animated avatar and enjoy the blood-splattered UI.
2. **Scan (🔍)**: Tim can help you look through your device's storage or "sniff out" new vocabulary from the internet.
3. **Settings (⚙️)**: View Tim's Brain Stats, manage permissions, and reset his memory.

---

## 💬 Chatting with Tim

Tim loves to talk, especially about **Brains** and **Technology**.

### 🧠 Special Commands
Type naturally or use specific keywords to trigger Tim's specialized logic:

- **`help`** or **`what can you do`**: Tim lists every command he knows (his "learning stuff" included).
- **`eat word <word>`**: Tells Tim to look up a specific word and add it to his vocabulary.
- **`vocabulary`** or **`brain stats`**: Shows a summary of what Tim has learned (words eaten, recently eaten, brain capacity, IQ).
- **`intelligence`**: Check Tim's current IQ and rank.
- **`magic 8 ball <question>`**: Ask Tim to predict the future!
- **`summarize`**, **`remember`**, or **`session`**: Tim recounts your current session *and* his long-term memory (your name, likes, and facts you've taught him).
- **`clear chat`**: Wipes Tim's short-term memory.

### 🧬 Teaching Tim
Tim learns permanently from plain sentences you type — no special syntax needed:
- **Facts**: *"the capital of France is Paris"* — he stores it and answers later questions like *"what is the capital of France?"*, even if you rephrase them.
- **Your name**: *"my name is …"* / *"call me …"* — he'll use it in greetings and recall it after restarts.
- **Your likes**: *"I like …"* — accumulated over time, not overwritten.
- **Your identity**: *"I am a developer"* — remembered for `who am i?`.
- New words from every message are absorbed in bulk; Tim quietly fetches real definitions for them in the background so he never quotes a placeholder at you.

### 📝 Personal Assistant
Tim can help you manage your decaying life with his proactive assistant capabilities:

#### Reminders
- **`remind me to [task] in [duration]`**: Set a relative reminder (e.g., "remind me to sharpen teeth in 2 hours" — minutes, hours, or days all work).
- **`remind me to [task] at [time]`**: Set a clock-time reminder (e.g., "remind me to eat brains at 5pm" or "at 17:30"). Past times roll to tomorrow.
- **`remind me to [task]`**: No time given? Tim defaults to about an hour from now.
- **`show reminders`**: Lists your upcoming reminders.

#### Tasks
- **`add task [description]`**: Add a new task (e.g., "add task fix the fence").
- **`show tasks`** or **`pending tasks`**: See your pending tasks with their IDs.
- **`overdue tasks`**: Check what you missed (Tim will judge you).
- **`complete task [id]`**: Mark a task as finished.

#### Notes
- **`take note [content]`**: Quickly save a note.
- **`show notes`** or **`my notes`**: List your saved notes.
- **`find note [query]`**: Search through your saved notes.
- **`daily summary`**: An at-a-glance summary of your day.

### 🌍 World Information
Ask Tim about the world around you:
- **`what time is it`** or **`current time`**: Get the current time with zombie flair.
- **`weather`** or **`weather in [city]`**: Check the weather (defaults to your location if no city specified).
- **`news`** or **`latest news`**: Get the latest headlines from the internet.
- **`stock [symbol]`**: Ask about stock prices (Tim has his own unique perspective on capitalism).

### 🩺 System Health (all platforms)
- **`system health`** or **`health check`**: Tim checks up on your device.
- **`check updates`**: Look for OS updates.
- **`run diagnostics`**: Check for device issues (disk, memory, CPU).
- **`update system`**: Install available updates (with Tim's guidance).

### 💻 System Integration (Desktop Only)
On Linux, Windows, and macOS, Tim can help with system tasks:
- **`system status`** or **`system info`**: Get a report about your system (OS, version, uptime, etc.).
- **`suggest tasks`** or **`what should I do`**: Platform-specific maintenance ideas.
- **`run command [command]`**: Execute system commands (Linux/Windows only).
- **`run admin command [command]`**: Run commands with administrator privileges (Linux/Windows only).

### 🔒 Security Monitoring
Tim can perform security audits on your system:
- **`security scan`** or **`check security`**: Perform a complete security audit including network and Bluetooth checks.
- **`check network`** or **`network status`**: Quick network overview showing active connections.
- **`check bluetooth`** or **`bluetooth status`**: Check Bluetooth devices and status.

### Interaction Tips
- **Talk about Brains**: He finds it highly engaging.
- **Loyalty**: Tim is a loyal subject. Treat him well!

---

## 🔍 The Scan Screen

Use this screen to help Tim "forage" for information on your device or the internet.

### File Hunting
- **Scan Brains (Internal)**: Scans the app's internal storage.
- **Scan Graveyard (External)**: Scans your device's external storage.
- **Sniff Directory**: Pick a specific folder for Tim to examine.
- **Chew File**: Have Tim examine a single file.

### Vocabulary Feasts
- **Mass Vocabulary Feast**: Tim reaches out to the internet and devours **5,000 random words** at once (fetched in parallel, then stored in one transaction) to boost his IQ instantly. Definitions are filled in from the dictionary API where available.

---

## ⚙️ Settings & Stats

The Settings screen has four sections:

### 🧠 Brain Stats
- **Conversations**, **Words Learned**, **Knowledge Base**, **Activities**, and **Database Size** — live counters for everything Tim remembers.

### 🔑 Permissions
- **Read Storage** / **Write Storage**: Status of the storage permissions Tim uses for file scanning.

### 🩺 System Health
Tim keeps an eye on the machine he's shambling around in:
- **Run Vitals Check**: Gathers a health report and shows a **Health Score** (0–100) along with:
    - **Disk Usage** — used percentage of total space
    - **Memory Usage** — used percentage of total RAM
    - **CPU Load** — current load percentage
    - **Uptime** — how long the device has been running
    - **Processes** — number of running processes
- **Detected Issues**: Any problems Tim sniffs out (low disk, heavy memory use, high load, etc.).
- **Install Updates**: Appears when Tim finds OS updates. Mobile platforms are report-only — Tim can only actually install desktop OS updates.

The same information is available from chat with **`system health`**, **`check updates`**, **`run diagnostics`**, and **`update system`**.

### 💀 Danger Zone
- **Clear Brain**: Deletes **all conversations, learned words, and knowledge** — a true reset for Tim's memory. (This cannot be undone!)

---

## 🆘 Support & Feedback

If Tim becomes too "braindead" or encounters an error:
1.  Go to **Settings** -> **Danger Zone** -> **Clear Brain** to reset his memory (conversations, words, and knowledge).
2.  Contact the creators at `darkworkllc@gmail.com`.

---

*Remember: Tim might be undead, but his passion for clean code is very much alive!* 🧟‍♂️💻
