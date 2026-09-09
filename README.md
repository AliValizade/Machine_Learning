# Machine Learning Coursework

A collection of machine learning coursework, programming assignments, and practical AI experiments developed with Python.

The repository combines academic machine learning exercises with practical experiments, including a Snake game project that explores manual, rule-based, and machine-learning-driven gameplay.

## Overview

This repository serves as an academic and practical archive of machine learning experiments.

It contains multiple coursework assignments as well as standalone experiments that explore how machine learning and artificial intelligence techniques can be applied to practical problems.

The repository currently includes:

* Machine learning coursework assignments
* Python-based experiments
* Data-driven programming exercises
* AI/game experiments
* A Snake game with multiple control strategies

## Repository Structure

```text
machine-learning-coursework/
├── Assignment_37/
├── Assignment_38/
├── Assignment_39/
├── Assignment_40/
├── Assignment_41/
├── Assignment_42/
├── Assignment_43/
├── Assignment_44/
├── Assignment_45/
├── Assignment_46/
├── Assignment_47/
├── Assignment_48/
├── Assignment_49/
├── Assignment_50/
│
└── Snake_AI_ML/
    ├── data/
    ├── modules/
    ├── generate_dataset.py
    ├── main_ai_conditions.py
    ├── main_manual.py
    ├── requirements.txt
    └── README.md
```

The assignment directories represent individual coursework exercises, while `Snake_AI_ML` is a more focused practical AI experiment.

## Snake AI Project

The `Snake_AI_ML` project explores different approaches to controlling the classic Snake game.

### 1. Manual Gameplay

The player controls the snake manually using keyboard input.

### 2. Rule-Based Gameplay

The snake can move automatically according to predefined conditions.

This approach demonstrates how a game agent can make decisions using explicit rules without machine learning.

### 3. Machine Learning-Based Gameplay

The project also explores using a dataset and machine learning techniques to determine the snake's actions.

The project includes functionality for:

* Generating gameplay data
* Storing game-state information
* Processing datasets
* Training/using machine learning models
* Controlling the game using learned behavior

The current project structure includes separate modules for manual and AI-based gameplay.

## Snake AI Data Pipeline

The machine-learning approach is based on game-state and action data.

A simplified workflow is:

```text
Game State
    ↓
Data Generation
    ↓
Dataset
    ↓
Data Processing
    ↓
Machine Learning Model
    ↓
Predicted Action
    ↓
Snake Movement
```

The project contains a `data/` directory for the generated dataset and a `modules/` directory for supporting components.

## Technologies

The repository uses Python and a range of libraries depending on the individual assignment.

The Snake AI project specifically uses technologies including:

* Python
* Arcade
* TensorFlow
* NumPy
* Pandas

## Learning Topics

The coursework and experiments provide practical exposure to concepts such as:

* Machine learning fundamentals
* Data preparation
* Model training
* Model evaluation
* Python programming
* Numerical computing
* Data manipulation
* Artificial intelligence
* Game programming
* Rule-based decision making
* Dataset generation
* Machine learning applied to games

## Academic Context

This repository is maintained as a coursework and experimentation archive.

The individual assignments represent academic exercises, while projects such as `Snake_AI_ML` demonstrate applying programming and machine learning concepts to a practical problem.

## Running the Snake AI Project

Clone the repository:

```bash
git clone https://github.com/AliValizade/machine-learning-coursework.git
cd machine-learning-coursework/Snake_AI_ML
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

The project contains separate entry points for manual and AI-based gameplay.

### Manual Mode

```bash
python main_manual.py
```

### AI / Rule-Based Mode

```bash
python main_ai_conditions.py
```

The exact machine-learning workflow depends on the dataset and model configuration included in the project.

## Project Status

This repository is primarily an **academic coursework and experimentation archive**.

Some assignments are standalone educational exercises, while `Snake_AI_ML` represents a more focused practical experiment combining game development and machine learning.

It should not be considered a production machine learning system.

## Future Improvements

Potential improvements include:

* Adding individual README files for important assignments
* Standardizing assignment structure
* Adding reproducible environment configuration
* Adding automated tests
* Improving experiment documentation
* Adding model evaluation metrics
* Documenting datasets in more detail
* Improving the Snake AI decision-making model
* Comparing multiple machine learning approaches
* Adding visualizations for training and evaluation results
* Adding GitHub Actions for automated testing

## Author

**Ali Valizade**

Python Developer | Django | AI, NLP & Automation | University Instructor

GitHub: https://github.com/AliValizade
