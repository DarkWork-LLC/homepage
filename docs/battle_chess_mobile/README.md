# ⚔️ BATTLE CHESS

A visceral, cartoon-style chess game built with **Flutter** and the **Flame engine**. Featuring chunky 3D-shaded vector pieces with big personalities, vibrant themes, and high-impact combat animations.

## Features

- **Gorgeous Visuals & Themes:**
  - **Board Themes:** Switch seamlessly between **Mahogany Wood**, **Imperial Marble**, **Neon Cyber**, and **Midnight Star** themes via the **Palette** icon in the top bar.
  - **Tactile 3D Board:** Rendered with tile bevels, inner shadows, theme-matched outer frames, and gold/metallic corner studs.
  - **Polished 3D-Shaded Vector Pieces:** Custom vector pieces painted with radial and linear gradients, specular highlights, glossy sheen, pedestals, and drop shadows.
  - **Last Move & Target Highlights:** Soft glowing trails on previous moves, pulsating selection glow, target lock reticles for captures, and glowing movement rings.
- **High-Impact FX & Fatalities:**
  - **Shockwave Rings & Comic Hit Text:** Captures unleash expanding shockwaves and animated floating text ("BOOM!", "SPLAT!", "FATALITY!", "CRUSH!", "KO!").
  - **Dust Puffs & Check Auras:** Landing dust particles when pieces hop, and a pulsating radial plasma check aura under kings in check.
  - **Unique Fatalities:** Every piece type has a unique death animation—pawns get squashed, rooks crumble, and queens explode into shards.
- **Sound & Music:** A soft, relaxing looped background track (`chess_loop.mp3`) plays quietly while the app runs, layered with punchy move blips and splatter audio on captures — all toggleable from the settings menu.
- **Learning AI**: Features a SQLite-backed adaptive learning system. The AI records every move you make and uses that experience to recognize tricks and adapt in future games. The database (`chess_learning.db`) is bounded to ~60,000 records to prevent performance degradation from unbounded growth.
- **Dynamic Personalities & Dorky Names:** Every game deals you a randomly named AI opponent (e.g. *Dr. Snoodlebottom*, *General Wobblepants*) with one of four play styles — *The Positionalist*, *The Heuristician*, *The Aggressor*, and *The Tactician*.
- **Five Difficulty Levels:** AI opponents are graded from 1 (Clueless) to 5 (Grandmaster). Beginner levels (1–2) use heavily randomized move selection, while levels 3–5 use progressively deeper minimax search with less randomness. Grandmaster (5) also recognizes a library of classic tactical patterns.
  - **Level 1 (Clueless):** No search; 60% chance of picking a random move from all legal moves.
  - **Level 2 (Toddler):** 2-ply search; 25% chance of picking a random move.
  - **Level 3 (Decent):** 3-ply search; 15% chance of picking a random move.
  - **Level 4 (Strategic):** 5-ply search; 5% chance of picking a random move.
  - **Level 5 (Grandmaster):** 7-ply search; detects and uses classic tactical patterns.
- **Battle Log & Adaptive Chat:** Real-time log of every move with interactive trash-talking AI that recognizes "tricks" it has seen before.
- **Multiplayer Options:**
  - **Local Network (Wi-Fi):** Host or join games over Wi-Fi/LAN for cross-platform head-to-head battles.
  - **Nearby Play (Bluetooth):** Head-to-head play over Bluetooth without Wi-Fi network required (via `nearby_connections`).
- **Undo & New Game:** Step back your last move (the AI's reply is rolled back too) or start a fresh game and pick White or Black at any time.
- **Full Chess Rules:** Legal move generation, castling, en passant, promotion, checkmate, and stalemate detection.

## License

**Proprietary License**

© 2026 **Dark Work, LLC** & **darkworkllc@gmail.com**. All rights reserved.
Created and owned by **Dark Work, LLC**. Unauthorized copying, modification, or distribution of this software is strictly prohibited.
