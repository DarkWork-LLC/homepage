# ⚔️ Battle Chess User Guide

Welcome to **Battle Chess**, the game where chess rules meet cartoon violence! This guide will help you set up your first game, customize your board theme, and master the "bloody" art of cartoon warfare.

## Game Summary

Battle Chess is not just a game of strategy; it's a spectacle. Every piece is a character with its own idle bobbing, breathing animations, and ground drop shadow. Moves aren't just slides—they are hops and leaps accompanied by landing dust. Captures aren't just removals—they are visceral, screen-shaking battles accompanied by shockwave rings, floating combat text ("BOOM!", "FATALITY!", "SPLAT!"), and unique piece-specific fatalities.

## How to Play

### Board Themes & Customization
Tap the **Palette Icon** in the top action bar to change the board theme at any time:
- **Mahogany Wood:** Classic warm wooden board with brass corner accents.
- **Imperial Marble:** Regal slate and white marble with gold highlights.
- **Neon Cyber:** Futuristic dark grid with glowing cyan and magenta lines.
- **Midnight Star:** Deep obsidian and silver starlight.

### Choosing Your Side
Before every match, you can choose to play as **White** or **Black**.
- **White:** You move first. The board is shown in standard orientation.
- **Black:** The computer or opponent moves first. The board is **inverted** so your Black pieces are at the bottom for better visibility.

### Moving Pieces
1. **Select a Piece:** Tap any of your pieces.
2. **View Highlights:** 
   - **Yellow Pulse:** Highlights your currently selected piece.
   - **Golden Trail:** Highlights the source and destination of the last move made.
   - **Green Circles:** Indicate open squares you can move to.
   - **Red Reticles:** Indicate enemy pieces you can capture.
3. **Confirm Move:** Tap a highlighted square to execute the move.
4. **Promote:** When a pawn reaches the far rank, a **Promote Pawn** picker appears so you can choose a Queen, Rook, Bishop, or Knight.

### Top Bar Controls
The top action bar holds the main controls:
- **Palette:** Opens the **Select Board Theme** sheet so you can switch between Mahogany Wood, Imperial Marble, Neon Cyber, and Midnight Star at any time.
- **Undo:** Take back your last move. Against the computer the AI's reply is rolled back too, so it is immediately your turn again.
- **Restart:** Start a fresh match; you are asked whether you want to play as **White** or **Black**.
- **Settings (gear, top-left):** Pick your opponent, toggle sound effects, or set up a Wi-Fi or Bluetooth game.

### Battles & Fatalities
When you move your piece onto a red-highlighted square, a **Fight** is triggered.
- Watch for the wind-up and the snap-lunge!
- The board flickers black at the moment of impact.
- An expanding **Shockwave Ring** and comic hit text ("BOOM!", "FATALITY!") pop up.
- The victim undergoes a unique death animation based on their type (e.g., the Rook crumbles, the Queen explodes).

### The Learning AI
Unlike standard chess apps, the computer here **learns** as you play.
- **Adapting to You:** If you beat the AI with a specific trick or opening, the AI records that experience. Next time it plays, it may recognize the situation and behave differently.
- **Persistent Knowledge:** The AI's experience is saved to a local database (`chess_learning.db`). The database is bounded to ~60,000 records to prevent performance degradation over time.
- **Personalities:** Each opponent is dealt a dorky, randomly generated name and one of four play styles: **The Positionalist** (position-focused), **The Heuristician** (classic heuristics), **The Aggressor** (prefers exchanges), and **The Tactician** (balanced minimax).

### Difficulty Levels
Opponents are graded 1–5. Beginner levels (1–2) are intentionally weak and randomized. Higher levels use deeper search with progressively less randomness.

| Level | Name | Search Depth | Random Move Chance | Notes |
|-------|------|--------------|-------------------|-------|
| 1 | **Clueless** | None (0-ply) | 60% | Plays essentially randomly; regular players will win easily. |
| 2 | **Toddler** | 2-ply | 25% | Still very weak; may make obvious mistakes. |
| 3 | **Decent** | 3-ply | 15% | Competent; occasional tactical awareness. |
| 4 | **Strategic** | 5-ply | 5% | Strong; plays solidly with minimal errors. |
| 5 | **Grandmaster** | 7-ply | 0% | Strongest; recognizes classic tactical patterns. |

### Battle Log & Chat
The bottom of the screen contains the **Battle Log**.
- **Move Tracking:** Every move is logged with turn numbers (e.g., "1. e2 → e4").
- **Trash Talk:** AI opponents will occasionally send dorky messages.
- **Chat:** Tap the "Trash talk here..." field to send messages to your opponent or the computer.

## Setting Up Games

Access the **Settings (gear icon)** in the top-left corner to choose your game mode and sound preferences.

### 1. Playing the Computer
Both computer opponents announce their name, personality, and difficulty level in the Battle Log when the game starts.
- **Computer (Random):** Varies greatly in skill from game to game, drawing from levels 3–5 (Decent, Strategic, Grandmaster) with full minimax search.
- **Computer (Basic):** A beginner-friendly opponent drawn from levels 1–2 (Clueless, Toddler). These opponents are intentionally very weak — they rarely take free pieces, often pick suboptimal moves, and regular players should have little trouble beating them.

### 2. Local Head-to-Head
- Select **Local Pass & Play (Human)** to play against someone sharing your device.

### 3. Local Network Multiplayer (Wi-Fi)
Play across two different devices on the same Wi-Fi/LAN network using **Host Local Game** or **Join Local Game**.

### 4. Nearby Play (Bluetooth)
Play head-to-head without needing a Wi-Fi network using **Nearby (Bluetooth)**. The app will ask for Bluetooth and location permissions the first time; these are only used to discover and connect to nearby devices.

### Sound & Music
A soft, relaxing background track (`chess_loop.mp3`) loops quietly while Battle Chess is running, with the arcade move and splatter effects layered on top. Toggle both together from **Settings → Sound: ON/OFF**. The music pauses automatically when the app is moved to the background and resumes when you return.

## Finishing a Game
- **Check** is announced in the status badge above the board.
- **Checkmate** ends the match with a victory dialog naming the winner and a **PLAY AGAIN** button.
- **Stalemate** ends the match as a draw.

---

© 2026 **Dark Work, LLC** & **darkworkllc@gmail.com**. Proprietary Software.
