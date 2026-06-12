import numpy as np
from itertools import islice

def get_possible_fits(puzzle: np.ndarray) -> dict:
    possibilities = dict()
    for i in range(81):
        if puzzle[i] == 0 :
            possibilities[i] = []
            for num in range(1, 10):
                fit = check_fit(puzzle, i, num)
                if fit: possibilities[i].append(num)
    return dict(sorted(possibilities.items(), key=lambda x: len(x[1])))

def solve(puzzle: np.ndarray, updater):
    possibilities = get_possible_fits(puzzle)
    recursive_backtracking(possibilities, puzzle, updater)

def recursive_backtracking(possibilities: dict, puzzle: np.ndarray, updater):
    zeros = np.count_nonzero(puzzle == 0)
    if zeros==0:
        return True
    pos = next(iter(possibilities))
    for number in possibilities[pos]:
        fit = check_fit(puzzle, pos, number)
        if fit:
            puzzle[pos] = number
            updater(number, pos)
            if recursive_backtracking(dict(islice(possibilities.items(), 1, None)), puzzle, updater): return True
            puzzle[pos] = 0
            updater(0, pos)
    return False

def check_fit(puzzle: np.ndarray, index: int, number: int)-> bool:
    #check row
    row = index//9
    row_i = row*9
    for i in range(9):
        if puzzle[row_i+i] == number:return False
    #check Column
    for i in range(9):
        if puzzle[index-9*i] == number:return False
    #check Box
    col = index-row_i
    box_i = (row//3*3)*9 + (col//3*3)  #index of the top left element of the box
    for c in range(3):
        for j in range(3):
            if puzzle[box_i+j+9*c] == number: return False
    return True