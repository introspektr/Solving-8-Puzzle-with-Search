from puzzle import PuzzleState


def heuristic_misplaced_tiles(state: PuzzleState) -> int:
    """
    Count the number of tiles that are not in their goal position.
    """
    goal = ['1', '2', '3', '4', '5', '6', '7', '8', 'b']
    return sum(
        1 for i, tile in enumerate(state.tiles)
        if tile != 'b' and tile != goal[i]
    )


def heuristic_manhattan_distance(state: PuzzleState) -> int:
    """
    Compute the total Manhattan distance of all tiles from their goal positions.
    """
    goal_positions = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), 'b': (2, 2)
    }

    total_distance = 0
    for index, tile in enumerate(state.tiles):
        if tile == 'b':
            continue
        current_row, current_col = divmod(index, 3)
        goal_row, goal_col = goal_positions[tile]
        total_distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return total_distance


def heuristic_wrong_column(state: PuzzleState) -> int:
    """
    Count the number of tiles that are not in their goal column.
    """
    # Goal columns for each tile (b ignored)
    goal_cols = {
        '1': 0, '2': 1, '3': 2,
        '4': 0, '5': 1, '6': 2,
        '7': 0, '8': 1   # blank is skipped
    }
    count = 0
    for index, tile in enumerate(state.tiles):
        if tile == 'b':
            continue
        current_col = index % 3
        if current_col != goal_cols[tile]:
            count += 1
    return count 