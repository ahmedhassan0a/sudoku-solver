import numpy as np
import requests

def fetch_puzzle(level: str) -> np.ndarray:
    headers = { "Referer": "https://sudoku.com/", "X-Requested-With": "XMLHttpRequest"}
    url = f"https://sudoku.com/api/v2/level/{level}"
    r = requests.get(url, headers=headers).json()
    puzzle = r["mission"]
    print(r["solution"])
    return np.array([int(num) for num in puzzle])
