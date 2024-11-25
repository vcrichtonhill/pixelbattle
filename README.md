# Battle Game with Pygame

A simple turn-based battle game built using the **Pygame** library. This game features two mages (White Mage and Black Mage) engaging in a magical duel. Players can attack or heal during their turns.
This project was assisted by a wonderful tutorial series by [Coding by Russ](https://www.youtube.com/watch?v=Vlolidaoiak&list=PLjcN1EyupaQnvpv61iriF8Ax9dKra-MhZ&ab_channel=CodingWithRuss). All art was drawn and owned by me.

## Features

- **Two characters**: White Mage (player controlled) and Black Mage (computer controlled).
- **Turn-based gameplay**: Player takes turns attacking or healing.
- **Dynamic animations**: Idle, attack, heal, hurt, and death animations for each character.
- **Health management**: Each mage has a health bar and limited healing abilities.

---
## Screenshots
### Battle Scene
![Two pixel style mages standing in a haunted forest.](/screenshots/ForestScreenshot.png "Optional Title")

### Actions
![Two pixel style mages battling in a haunted forest. The white mage is attacking the other wit ha fireball spell.](/screenshots/AttackScreenshot.png "Optional Title")

---

## How to Play

1. **Attack**: Hover over the enemy mage and click to attack. 
   - The cursor changes to a fireball to indicate an attack action.
2. **Heal**: Hover over your own mage and click to heal.
   - The cursor changes to a heal spell icon to indicate a heal action.
3. **Win Condition**: Reduce the enemy mage’s HP to zero to win the game.

---

## Requirements

- Python 3.6 or higher
- Pygame library (install with `pip install pygame`)
- Assets:
  - **Background**: `assets/background.png`
  - **Panel**: `assets/panel.png`
  - **Fireball Cursor**: `assets/Fireball.png`
  - **Heal Spell Icon**: `assets/healspell.png`
  - **Character Sprites**: Located in `assets/sprites/<character_name>`

---

## Installation

1. Clone the repository or download the code.
2. Ensure the required assets are in the `assets` folder.
3. Install the Pygame library:
   ```bash
   pip install pygame
