# Snake Game

Welcome to the Snake Game, a classic arcade game built with Python and Tkinter. The objective of the game is to navigate the snake, collect food items, and grow longer while avoiding collisions with the walls or the snake's own body. This project is an excellent example for learning basic game development and graphical programming with Tkinter.

## Table of Contents

- [Introduction](#introduction)
- [Game Features](#game-features)
- [Installation](#installation)
- [Usage](#usage)
- [How to Play](#how-to-play)
- [Game Mechanics](#game-mechanics)
- [Code Overview](#code-overview)
  - [Game Variables](#game-variables)
  - [Snake Class](#snake-class)
  - [Food Class](#food-class)
  - [Movement Functions](#movement-functions)
  - [Window Adjustment](#window-adjustment)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Snake Game is a timeless classic that many of us have enjoyed playing on early mobile devices. This project recreates the game using Python's Tkinter library, providing a graphical user interface and interactive gameplay. The game is simple yet engaging, making it an ideal project for beginners in Python programming.

## Game Features

- **Intuitive Controls**: Control the snake using the arrow keys.
- **Score Display**: The current score is displayed at the top of the game window.
- **Dynamic Gameplay**: The snake grows in length with each food item collected, increasing the game's difficulty.
- **Restart Functionality**: Easily restart the game using the restart button.
- **Game Over Screen**: Displays a "Game Over" message when the snake collides with the wall or itself.

## Installation

To get started with the Snake Game, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   ```

2. **Ensure Python is Installed**:
   Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

3. **Run the Game**:
   ```bash
   python snake_game.py
   ```

## Usage

Once you have cloned the repository and ensured Python is installed, you can run the game by executing the `snake_game.py` script. The game window will open, and you can start playing immediately.

## How to Play

1. **Starting the Game**: Run the `snake_game.py` script. The game window will appear with the snake and a food item.
2. **Controlling the Snake**: Use the arrow keys on your keyboard to control the direction of the snake:
   - **Up Arrow**: Move up
   - **Down Arrow**: Move down
   - **Left Arrow**: Move left
   - **Right Arrow**: Move right
3. **Objective**: Guide the snake to collect food items. Each food item collected increases your score and makes the snake grow longer.
4. **Avoid Collisions**: Prevent the snake from colliding with the walls or its own body. A collision will result in a game over.
5. **Restarting the Game**: Click the "Restart" button to start a new game at any time.

## Game Mechanics

### Game Variables

- `GAME_HEIGHT`: Height of the game window.
- `GAME_WIDTH`: Width of the game window.
- `GAME_SPACE`: Size of each step the snake takes.
- `SPEED_RANGE`: Speed of the snake's movement.
- `SNAKE_COLOR`: Color of the snake.
- `SNAKE_SIZE`: Initial size of the snake.
- `FOOD_COLOR`: Color of the food.
- `BACKGROUND_COLOR`: Background color of the game window.
- `DIRECTION`: Initial direction of the snake.
- `score`: Initial score of the game.

### Snake Class

The `Snake` class initializes the snake's body, coordinates, and graphical representation. It manages the snake's size and position on the canvas.

### Food Class

The `Food` class generates food items at random positions on the game canvas. It handles the graphical representation of the food.

### Movement Functions

- `move_snake()`: Moves the snake in the current direction, checks for food collection, and updates the score. It also checks for collisions and handles the game over condition.
- `restart_game()`: Resets the game state, including the score, snake, and food.
- `game_over()`: Displays the "Game Over" message when the snake collides with the wall or itself.
- `change_direction(new_dir)`: Changes the direction of the snake based on user input.
- `check_collision(snake)`: Checks for collisions with the walls and the snake's own body.

### Window Adjustment

The game window is created using Tkinter and adjusted for optimal display on the screen. The window's size and position are set to ensure the game is centered on the screen.

## Screenshots

Here are some screenshots of the game:

![Game Start](screenshots/start.png)
*Initial game screen with the starting score.*

![In-Game](screenshots/in_game.png)
*In-game screenshot showing the snake and a food item.*

![Game Over](screenshots/game_over.png)
*Game over screen displayed after a collision.*

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request. Here’s how you can contribute:

1. **Fork the repository** on GitHub.
2. **Clone your fork**:
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   ```
3. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature-or-bugfix-name
   ```
4. **Commit your changes**:
   ```bash
   git commit -am 'Add new feature or fix bug'
   ```
5. **Push to the branch**:
   ```bash
   git push origin feature-or-bugfix-name
   ```
6. **Create a pull request** on GitHub and describe your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
 
