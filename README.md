# 5x5 Tic Tac Toe Game

A Python implementation of the classic Tic Tac Toe game with a 5x5 board, save/load functionality, and a console-based interface.

## Features

- **5x5 Game Board**: Larger board for extended gameplay
- **Two Player Mode**: Play with a friend on the same computer
- **Save/Load System**: Continue your game anytime
- **Win Detection**: Automatic winner checking for rows, columns, and diagonals
- **Draw Detection**: Game recognizes when the board is full
- **Player Statistics**: Track player names and symbols

## How to Play

1. Run the game using `python game.py`
2. Choose to start a new game or load a saved one
3. Enter player names when starting a new game
4. Players take turns entering row and column numbers (1-5)
5. The first player to get 5 in a row (horizontal, vertical, or diagonal) wins!
6. If all spaces are filled with no winner, the game ends in a draw

## Game Controls

- Enter numbers 1-5 for row and column selection
- Menu navigation with numbers 1-3
- Automatic saving after each move

## File Structure

- `game.py` - Main game logic and flow
- `player.py` - Player class definition
- `board.py` - Board management and win checking
- `save_game.py` - Save/load functionality
- `saves/` - Directory for saved game files

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Ensure you have Python 3 installed
2. Download all game files to the same directory
3. Run `python game.py` to start playing

## Saving and Loading

The game automatically saves after each move. To continue a previous game, select "Load Game" from the main menu. Saved games are stored in the `saves` directory as `current_game.json`.