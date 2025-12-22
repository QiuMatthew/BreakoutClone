# Breakout Clone

## Overview
Breakout Clone is a modern implementation of the classic arcade game "Breakout." In this game, you control a paddle to bounce the ball and destroy bricks. Some bricks have power-ups that can modify the paddle size, enhancing the gameplay experience.

This project is written in Python and uses the **pygame** library for rendering graphics and game logic.

---

## Features
- **Classic Breakout Gameplay**: Destroy all the bricks to win.
- **Power-ups**: Bricks can modify the paddle size, making the game more dynamic.
- **Restart and Quit Options**: Replay the game or exit using keyboard commands.

---

## How to Play
- **Move the Paddle**: Use the left and right arrow keys to control your paddle.
- **Win Condition**: Break all the bricks to win.
- **Lose Condition**: Let the ball fall below the paddle.
- **Restart**: Press <kbd>R</kbd> after losing to restart the game.
- **Quit**: Press <kbd>Q</kbd> to quit.

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/breakout-clone.git
   ```
2. Navigate to the project folder:
   ```bash
   cd breakout-clone
   ```
3. Install the required dependencies:
   ```bash
   pip install pygame
   ```
4. Run the game:
   ```bash
   python main.py
   ```

---

## File Structure
```
.
├── src/                # Source code
├── assets/             # (Optional) Images, sounds, etc.
├── tests/              # (Optional) Unit tests
├── main.py             # Entry point of the game
├── requirements.txt    # Dependency list
└── README.md           # Project documentation
```

---

## Future Improvements
- [ ] Add sound effects for collisions.
- [ ] Add more power-ups (e.g., multiple balls, speed changes).
- [ ] Add multiple levels with increasing difficulty.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
