import numpy as np
from itertools import islice
from numpy import ndarray
from puzzle_fetcher import fetch_puzzle


def get_possible_fits(puzzle: np.ndarray) -> dict:
    possibilities = dict()
    for i in range(9):
        for j in range(9):
            if puzzle[i, j] == 0 :
                possibilities[i*10+j] = []
                for num in range(10):
                    if check_fit(puzzle, (i, j), num):
                        possibilities[i*10+j].append(num)
    return possibilities

def solve(puzzle: np.ndarray, updater):
    possibilities = get_possible_fits(puzzle)
    recursive_backtracking(possibilities, puzzle, updater)

def recursive_backtracking(possibilities: dict, puzzle: ndarray, updater):
    zeros = np.count_nonzero(puzzle == 0)
    if zeros==0:
        return True
    k = next(iter(possibilities))
    i = k // 10
    j = k % 10
    for number in possibilities[k]:
        if check_fit(puzzle, (i, j), number):
            puzzle[i, j] = number
            updater(number, i, j)
            if recursive_backtracking(dict(islice(possibilities.items(), 1, None)), puzzle, updater): return True
            puzzle[i,j] = 0
            updater(0, i, j)

    return False

def check_fit(puzzle: np.ndarray, index: tuple, number: int)-> bool:
    fits = True
    #check Row fit
    for j in range(9):
        if puzzle[index[0], j] == number:return False

    #check Collumn fit
    for i in range(9):
        if puzzle[i, index[1]] == number: return False

    #check Box fit
    start_row = (index[0] // 3) * 3
    start_col = (index[1] // 3) * 3
    for i in range(3):
        for j in range(3):
            if puzzle[start_row + i, start_col + j] == number: return False

    return fits