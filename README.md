# 🪨 Mancala — Python Console Game

A simple Python implementation of the classic **Mancala** board game, playable by **two humans**, **two CPU players**, or **one human vs. CPU**. The computer player uses a depth-limited **minimax search** strategy to determine its moves.

---

## 📌 Features

- Turn-based Mancala gameplay with full rules:
  - Sowing, captures, extra turns, and endgame handling
- Supports three play modes:
  - Human vs Human
  - Human vs CPU
  - CPU vs CPU
- CPU uses **minimax-based decision making** with adjustable search depth
- Console-rendered board with clear layout
- Input validation and helpful prompts
- Final score calculation and winner announcement

---

## 🧠 CPU Logic (Minimax)

The CPU player uses a **minimax algorithm** to evaluate possible future moves. It recursively simulates turns up to a given depth and chooses the move that maximizes its advantage while assuming the opponent plays optimally in return. By default, the CPU hardness is set to 5, meaning it will simulate up to 5 moves in advance when determining the best move. This can be changed in the ```get_cpu_move()``` function, as indicated in the comments as well.


## ▶️ How to Play

Run the game with:

```bash
python main.py
```
Follow the prompts and play the game with the usual rules, which can be referenced [here](https://www.scholastic.com/content/dam/teachers/blogs/alycia-zimmerman/migrated-files/mancala_rules.pdf). In this implementation of mancala, both players' pits are numbered 1 through 6, from left to right as seen from each player's point of view. 




