import heapq
from typing import Callable, Optional, List
from puzzle import PuzzleState, GOAL_STATE


def greedy_best_first_search(
    start_state: PuzzleState,
    heuristic: Callable[[PuzzleState], int],
    max_steps: int = 10000
) -> Optional[List[PuzzleState]]:
    """
    Perform Greedy Best-First Search from start_state using the given heuristic.
    Prioritizes nodes purely by heuristic value (h(n)).
    Returns the solution path if found, otherwise None.
    """
    # Use a tuple of (h_cost, unique_id, state) to avoid direct PuzzleState comparisons
    frontier: List[tuple[int, int, PuzzleState]] = []
    explored: set[PuzzleState] = set()

    # Initialize start state's heuristic
    start_state.h_cost = heuristic(start_state)
    # Push with a unique tie-breaker onto the frontier
    heapq.heappush(frontier, (start_state.h_cost, id(start_state), start_state))

    steps = 0
    # Use shared constant for goal state
    goal_tiles = GOAL_STATE

    while frontier and steps < max_steps:
        # Unpack h_cost, unique_id, then state from the frontier
        _, _, current = heapq.heappop(frontier)

        if current.tiles == goal_tiles:
            return current.reconstruct_path()

        explored.add(current)

        for successor in current.get_successors():
            if successor in explored:
                continue

            successor.h_cost = heuristic(successor)
            # Add new state to frontier
            heapq.heappush(frontier, (successor.h_cost, id(successor), successor))

        steps += 1

    return None  # No solution found within max_steps 