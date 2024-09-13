
# Snake Game Project

## Overview

This project implements the classic Snake game using Python and the Arcade library. The game is developed in three distinct methods:

1. **Manual Gameplay**: Players control the snake using keyboard inputs.
2. **Automated Gameplay with Conditions**: The snake moves automatically based on predefined conditions.
3. **Machine Learning-Based Gameplay**: The snake's movements are determined using a dataset and machine learning algorithms.

## Requirements

- Python 3.x
- Arcade library (`pip install arcade`)
- TensorFlow (`pip install tensorflow`) for machine learning-based gameplay
- pandas (`pip install pandas`) for data handling
- numpy (`pip install numpy`) for numerical operations

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/snake-game-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd snake-game-project
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Manual Gameplay

Run the following script to play the game manually:
```bash
python manual_gameplay.py
```
Use the arrow keys to control the snake.

### 2. Automated Gameplay with Conditions

Run the following script for automated gameplay based on conditions:
```bash
python automated_gameplay_conditions.py
```
The snake's movement is determined by the implemented conditions.

### 3. Machine Learning-Based Gameplay

Run the following script to train the model and play the game using machine learning:
```bash
python ml_gameplay.py
```
Ensure you have prepared the dataset and trained the model as required.

## Dataset

For the machine learning-based gameplay, a dataset is used to train the model. The dataset should include records of snake movements and game state information.

- You can generate your own dataset by running the automated gameplay and storing the state-action pairs.
- Place the dataset in the `data/` directory, and the model training script will automatically use it.

## Example

Here is an example of how the game looks in action:

![Snake Game Example](data/)

## Contributing

Feel free to contribute to the project by creating pull requests or reporting issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the Arcade library for providing an easy-to-use platform for game development.
- Any additional contributors or resources used.
