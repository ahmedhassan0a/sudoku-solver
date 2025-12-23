import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from numpy import ndarray
from puzzle_fetcher import fetch_puzzle
from solver import solve


window = ctk.CTk()
window.geometry("800x600")
window.title("Sudoku Solver")

header = ctk.CTkLabel(master=window,
                      width=30,
                      text_color="white",
                      text="Sudoku Solver",
                      font=("Arial", 28))
header.configure(pady=14)
grid_frame = ctk.CTkFrame(window,
                          width= 600,
                          )
levels = ["Easy", "Medium", "Hard", "Expert", "Master", "Extreme"]
cells = []

def update_grid(number, i, j):
    display_val = int(number) if number != 0 else ""
    cells[i][j].configure(text=display_val)
    window.update()

puzzle, solution = fetch_puzzle("Easy")
def sellect_difficulity(level: str):
    if level == "Master": level = "evil"
    k = fetch_puzzle(level)
    puzzle[:] = k[0][:]
    solution[:] = k[1][:]
    for i in range(9):
        for j in range(9):
            update_grid(puzzle[i, j], i, j)

button_frame = ctk.CTkFrame(master= window)

# Make the level select buttons
for level in levels:
    btn = ctk.CTkButton(
        button_frame,
        text=level,
        width=80,
        command=lambda l=level: sellect_difficulity(l)
    )
    btn.pack(side="left", padx=5, expand=True)

# Make the 9x9 grid
for i in range(9):
    row_widgets = []
    for j in range(9):
        cell = ctk.CTkLabel(
            grid_frame,
            text=int(puzzle[i, j]) if puzzle[i, j]!=0 else "",
            width=45, height=45,
            fg_color="#434343",
            corner_radius=2,
        )
        cell.grid(row=i, column=j, padx=1, pady=1)
        row_widgets.append(cell)
    cells.append(row_widgets)

# Make the "Solve" button
solve_button = ctk.CTkButton(
        master=window,
        text="Solve",
        width=80,
        height=40,
        command=lambda x=0: solve(puzzle, update_grid)
    )

header.pack()
button_frame.pack(pady=2, padx=1)
grid_frame.pack(pady=20, padx=20)
solve_button.pack(pady=20)
window.mainloop()

# sellect_difficulity("Extreme")
# solve(puzzle, update_grid)