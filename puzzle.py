from typing import List, Optional
import random

# Goal configuration for the 8-puzzle
GOAL_STATE = ['1', '2', '3', '4', '5', '6', '7', '8', 'b']

class PuzzleState:
    """
    Represents a single state of the 8-puzzle.
    """

    def __init__(self, tiles: List[str], g_cost: int = 0, h_cost: int = 0, parent: Optional['PuzzleState'] = None):
        self.tiles = tiles
        self.blank_index = tiles.index('b')
        self.g_cost = g_cost  # cost to reach this node (used in A* search)
        self.h_cost = h_cost  # heuristic estimate to goal
        self.parent = parent  # reference to the parent PuzzleState

    def __eq__(self, other):
        if not isinstance(other, PuzzleState):
            return False
        return self.tiles == other.tiles

    def __hash__(self):
        return hash(tuple(self.tiles))

    def get_successors(self) -> List['PuzzleState']:
        """
        Generate all valid successor states by moving the blank tile.
        """
        successors = []
        # Directions: (name, delta index)
        moves = {
            'up': -3,
            'down': 3,
            'left': -1,
            'right': 1
        }

        row, col = divmod(self.blank_index, 3)

        for direction, delta in moves.items():
            new_index = self.blank_index + delta

            if direction == 'up' and row == 0:
                continue
            if direction == 'down' and row == 2:
                continue
            if direction == 'left' and col == 0:
                continue
            if direction == 'right' and col == 2:
                continue

            # Swap blank with the target tile
            new_tiles = self.tiles.copy()
            new_tiles[self.blank_index], new_tiles[new_index] = new_tiles[new_index], new_tiles[self.blank_index]

            # Create new PuzzleState
            successor = PuzzleState(
                tiles=new_tiles,
                g_cost=self.g_cost + 1,  # Increment g-cost for A*
                parent=self
            )
            successors.append(successor)

        return successors

    def reconstruct_path(self) -> List['PuzzleState']:
        """
        Reconstruct the full path from the start state to this state.
        """
        path = []
        current = self
        while current:
            path.append(current)
            current = current.parent
        return list(reversed(path))

    def display(self):
        """
        Utility function to print the state in a 3x3 grid format.
        """
        for i in range(0, 9, 3):
            print(' '.join(self.tiles[i:i+3]))
        print()

def count_inversions(tiles: List[str]) -> int:
    """
    Count the number of inversions in the tile list.
    An inversion is a pair of tiles (a, b) such that a precedes b but a > b.
    The blank ('b') is ignored for the purposes of counting inversions.
    """
    inversion_count = 0
    tile_numbers = [tile for tile in tiles if tile != 'b']

    for i in range(len(tile_numbers)):
        for j in range(i + 1, len(tile_numbers)):
            if int(tile_numbers[i]) > int(tile_numbers[j]):
                inversion_count += 1

    return inversion_count

def is_solvable(tiles: List[str]) -> bool:
    """
    Determine if a puzzle configuration is solvable based on inversion count.
    For a 3x3 8-puzzle, the puzzle is solvable if the number of inversions is even.
    """
    inversions = count_inversions(tiles)
    return inversions % 2 == 0

def generate_random_state() -> List[str]:
    """
    Generate a random, solvable starting configuration for the 8-puzzle.
    """
    tiles = ['1', '2', '3', '4', '5', '6', '7', '8', 'b']

    while True:
        random.shuffle(tiles)
        if is_solvable(tiles):
            return tiles.copy()  # Return a copy to avoid accidental mutation 