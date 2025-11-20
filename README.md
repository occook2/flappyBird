# Flappy Bird AI

An AI-powered Flappy Bird game that uses NEAT (NeuroEvolution of Augmenting Topologies) to train neural networks to play the game through evolutionary algorithms.

## Prerequisites

- Python 3.10 or 3.11 (recommended)
- Conda (optional but recommended for environment management)

## Installation

### Option 1: Using Conda (Recommended)

1. **Create a new conda environment:**
   ```powershell
   conda create -n flappybird python=3.10
   ```

2. **Activate the environment:**
   ```powershell
   conda activate flappybird
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

### Option 2: Using pip with virtual environment

1. **Create a virtual environment:**
   ```powershell
   python -m venv venv
   ```

2. **Activate the environment:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

## Configuration

The NEAT algorithm configuration is located in `config-feedforward.txt`. This file controls:
- Population size
- Fitness threshold
- Neural network structure
- Mutation rates
- Species parameters

You can modify these settings to adjust the AI's learning behavior.

## Running the Project

To start training the AI:

```powershell
python src/App.py
```

The AI will begin training through multiple generations, with statistics displayed in the console. The game window will show the birds learning to navigate through the pipes.

## How It Works

- **src/App.py**: Main entry point that initializes the NEAT algorithm and starts the training process
- **src/Game.py**: Core game logic and AI integration
- **src/Bird.py**: Bird character class with physics
- **src/Pipe.py**: Obstacle generation and movement
- **src/Ground.py**: Ground rendering and scrolling
- **src/Window.py**: Display and rendering management
- **config-feedforward.txt**: NEAT algorithm configuration

The AI uses neural networks to decide when to jump, with fitness scores based on survival time and score. Better-performing birds pass their genes to the next generation, gradually improving performance.

## Dependencies

- **pygame 2.5.2**: Game engine and graphics
- **neat-python 0.92**: NEAT genetic algorithm implementation

## Project Structure

```
flappyBird/
├── src/                        # Source code
│   ├── App.py                  # Main entry point
│   ├── Game.py                 # Game logic
│   ├── Bird.py                 # Bird class
│   ├── Pipe.py                 # Pipe obstacles
│   ├── Ground.py               # Ground rendering
│   └── Window.py               # Display management
├── imgs/                       # Game assets
├── config-feedforward.txt      # NEAT configuration
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```
