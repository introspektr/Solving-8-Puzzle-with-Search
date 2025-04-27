# 8-Puzzle Solver: Informed Search Algorithms

This project implements Greedy Best-First Search and A* Search to solve the classic 8-puzzle problem, using multiple heuristics.

## Features

- **Search Algorithms:** Greedy Best-First Search, A* Search
- **Heuristics:** Misplaced Tiles, Manhattan Distance, Wrong Column
- **Random Solvable Start States:** Generates 5 random, solvable puzzles per run
- **Performance Reporting:** Prints solution paths, move counts, and averages
- **Modular Codebase:** Each algorithm and heuristic in its own file

## Requirements

- Python 3.7 or higher (no external dependencies)

## How to Run

1. **Clone the repository:**
    ```bash
    git clone https://github.com/introspektr/Solving-8-Puzzle-with-Search
    cd Solving-8-Puzzle-with-Search
    ```

2. **Run the main script:**
    ```bash
    python main.py
    ```

3. **View the results:**
    - All output is written to `output.txt` in the project directory.
    - Open `output.txt` to inspect solution paths, move counts, and averages.

## File Structure

- `main.py` — Driver script; runs experiments and writes results to `output.txt`
- `puzzle.py` — Puzzle state representation, inversion/solvability checks, random state generator
- `heuristics.py` — Heuristic functions
- `greedy_search.py` — Greedy Best-First Search implementation
- `a_star_search.py` — A* Search implementation
- `output.txt` — Results from the latest run

## Customization

- To see all solution steps in the console, set `verbose=True` in `main.py`.
- To change the number of random puzzles, edit the value in `main.py` (`start_states = [...]`).
- To add new heuristics, define them in `heuristics.py` and add to the `heuristics` dictionary in `main.py`.

## Notes

- The program is designed for the 8-puzzle (3x3).
- The random seed is not fixed; results will vary on each run. 