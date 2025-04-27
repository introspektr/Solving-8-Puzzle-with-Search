import heapq
from typing import Callable, Optional, List
from puzzle import PuzzleState, GOAL_STATE


def a_star_search(
    start_state: PuzzleState,
    heuristic: Callable[[PuzzleState], int],
    max_steps: int = 10000
) -> Optional[List[PuzzleState]]:
    """
    Perform A* Search from start_state using the given heuristic.
    Prioritizes nodes by f(n) = g(n) + h(n).
    Returns the solution path if found, otherwise None.
    """
    # Use a tuple of (f_cost, unique_id, state) to avoid direct PuzzleState comparisons
    frontier: List[tuple[int, int, PuzzleState]] = []
    explored: set[PuzzleState] = set()

    # Initialize start state's heuristic and push with f_cost
    start_state.h_cost = heuristic(start_state)
    start_state.g_cost = 0
    # Push with f_cost and a unique tie-breaker onto the frontier
    heapq.heappush(frontier, (start_state.g_cost + start_state.h_cost, id(start_state), start_state))

    steps = 0
    goal_tiles = GOAL_STATE

    while frontier and steps < max_steps:
        # Unpack f_cost, unique_id, then state from the frontier
        _, _, current = heapq.heappop(frontier)

        if current.tiles == goal_tiles:
            return current.reconstruct_path()

        explored.add(current)

        for successor in current.get_successors():
            if successor in explored:
                continue

            successor.g_cost = current.g_cost + 1
            successor.h_cost = heuristic(successor)
            total_cost = successor.g_cost + successor.h_cost
            # Add new state to frontier
            heapq.heappush(frontier, (total_cost, id(successor), successor))

        steps += 1

    return None  # No solution found within max_steps 