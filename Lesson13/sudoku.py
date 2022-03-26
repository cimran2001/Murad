from typing import List, Tuple, Optional
from pprint import pprint

sudoku = [
    [0, 0, 9,   0, 0, 0,   0, 0, 0],
    [0, 0, 0,   3, 0, 0,   0, 1, 0],
    [0, 4, 5,   0, 1, 0,   0, 0, 6],
        
    [0, 0, 0,   0, 0, 8,   2, 0, 0],
    [0, 6, 1,   0, 3, 0,   0, 0, 5],
    [7, 0, 0,   0, 0, 0,   0, 0, 0],
        
    [9, 0, 0,   0, 4, 0,   0, 0, 0],
    [0, 7, 4,   2, 0, 0,   5, 0, 0],
    [3, 0, 0,   0, 0, 0,   0, 0, 7]
]


def find_empty(puzzle: List[List[int]]) -> Optional[Tuple[int, int]]:
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col] == 0:
                return (row, col)
    return None


def is_avail(puzzle: List[List[int]], pos: Tuple[int, int], value: int) -> bool:
    row, col = pos
    
    if value in puzzle[row]: # checking row
        return False

    column = [puzzle[i][col] for i in range(9)]
    if value in column: # checking column
        return False
    
    
    start_row = row - row % 3
    start_col = col - col % 3
    
    for i in range(3): # checking little square
        for j in range(3):
            if puzzle[start_row + i][start_col + j] == value:
                return False
            
    return True


def solve(puzzle: List[List[int]]) -> bool:
    empty_pos = find_empty(puzzle)
    if empty_pos is None:
        return True
    
    for i in range(1, 10):
        if is_avail(puzzle, empty_pos, i) is False:
            continue
        
        row, col = empty_pos
        puzzle[row][col] = i
        
        result = solve(puzzle)
        if result is True:
            return True
        
        puzzle[row][col] = 0
    
    return False


result = solve(sudoku)


if result is False:
    print("Sudoku is not solvable")
else:
    pprint(sudoku)
