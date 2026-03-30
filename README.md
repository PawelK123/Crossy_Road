# 🐢 Crossy Road

A Python clone of the classic Crossy Road game built with the `turtle` module. Guide your turtle safely across a busy road — each level gets faster!

---

## 📋 Requirements

- Python 3.x
- No external libraries required (uses only the built-in `turtle` module)

---

## 🚀 How to Run

```bash
python main.py
```

---

## 🎮 How to Play

1. A turtle appears at the bottom of the screen
2. Press **↑ (Up Arrow)** to move forward
3. Avoid the cars coming from the right
4. Reach the finish line at the top to advance to the next level
5. Each new level increases the car speed
6. The game ends when a car hits the turtle

---

## 🏗️ Code Structure

### `main.py`
Entry point of the game. Sets up the screen, initializes all objects, and runs the main game loop — handling movement, collision detection, and level progression.

### `Player` — `player.py`

| Method | Description |
|---|---|
| `move()` | Moves the turtle forward by 10 units |
| `is_at_finish_line()` | Returns `True` if the turtle reached the top |
| `go_to_start()` | Resets the turtle to the starting position |

### `CarManager` — `car_manager.py`

| Method | Description |
|---|---|
| `create_car()` | Randomly spawns a new car on the right side |
| `move()` | Moves all cars to the left |
| `level_up()` | Increases car speed by 10 units |

### `Scoreboard` — `scoreboard.py`

| Method | Description |
|---|---|
| `score_up()` | Increments the level counter and refreshes display |
| `update_scoreboard()` | Redraws the level text on screen |
| `end_game()` | Displays "Game Over" in the center of the screen |

---

