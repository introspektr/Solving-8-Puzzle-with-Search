from puzzle import PuzzleState, generate_random_state
import contextlib
from heuristics import heuristic_misplaced_tiles, heuristic_manhattan_distance, heuristic_wrong_column
from greedy_search import greedy_best_first_search
from a_star_search import a_star_search


def run_experiments(verbose: bool = False):
    """
    Run search experiments across multiple heuristics and initial states.

    verbose: if True, display each intermediate state in the solution path.
    """
    heuristics = {
        "Misplaced Tiles": heuristic_misplaced_tiles,
        "Manhattan Distance": heuristic_manhattan_distance,
        "Wrong Column": heuristic_wrong_column,
        # "Custom Heuristic": heuristic_custom,  # Add this later easily
    }

    algorithms = {
        "Greedy Best-First Search": greedy_best_first_search,
        "A* Search": a_star_search,
    }

    # Generate 5 random solvable starting states
    start_states = [generate_random_state() for _ in range(5)]

    goal_tiles = ['1', '2', '3', '4', '5', '6', '7', '8', 'b']

    for algo_name, search_func in algorithms.items():
        print(f"\n===== {algo_name} =====\n")

        for heuristic_name, heuristic_func in heuristics.items():
            print(f"\n--- Heuristic: {heuristic_name} ---\n")
            path_lengths = []

            for idx, tiles in enumerate(start_states, 1):
                print(f"Start State {idx}:")

                start = PuzzleState(tiles.copy())  # Copy to avoid mutation
                result = search_func(start, heuristic_func)

                if result:
                    moves = len(result) - 1
                    print(f"Solution found in {moves} moves.")
                    path_lengths.append(moves)

                    # Print full path only if verbose
                    if verbose:
                        for step in result:
                            step.display()
                else:
                    print("No solution found.")
                    path_lengths.append(float('inf'))  # Mark unsolved cases

            # Compute average number of steps (ignoring unsolved cases)
            solved_lengths = [l for l in path_lengths if l != float('inf')]

            if solved_lengths:
                average_steps = sum(solved_lengths) / len(solved_lengths)
                print(f"\nAverage number of steps: {average_steps:.2f}\n")
            else:
                print("\nNo solvable paths found for this heuristic.\n")


if __name__ == "__main__":
    """
    Entry point for running the 8-Puzzle Search Experiments.
    """
    # Set verbose=False to suppress per-step boards
    with open("output.txt", "w") as f:
        with contextlib.redirect_stdout(f):
            print("Starting 8-Puzzle Search Experiments...\n")
            run_experiments(verbose=False) 