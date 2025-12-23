import requests
from numpy import ndarray


def fetch_puzzle(level: str) -> ndarray:
    headers = { "Referer": "https://sudoku.com/", "X-Requested-With": "XMLHttpRequest"}
    url = f"https://sudoku.com/api/v2/level/{level}"
    r = requests.get(url, headers=headers).json()
    puzzle = r["mission"]
    solution = r["solution"]
    return convert_to_array(puzzle), convert_to_array(solution)

def convert_to_array(numbers: str) -> ndarray:
    fin = ndarray((9, 9))
    for i in range(9):
        for j in range(9):
            fin[i, j] = numbers[i*9 + j]
    return fin