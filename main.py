import tkinter as tk
from tkinter import messagebox

from solver import solve_n_queens
from board import draw_board


# ---------------- GLOBAL VARIABLES ---------------- #

solutions = []
current_index = 0
current_n = 0


# ---------------- SOLVER FUNCTION ---------------- #

def start_solver():

    global solutions
    global current_index
    global current_n

    try:

        n = int(entry.get())

        if n < 4:
            messagebox.showerror(
                "Error",
                "N must be at least 4"
            )
            return

        if n > 12:
            messagebox.showerror(
                "Error",
                "Maximum allowed is 12"
            )
            return

    except:

        messagebox.showerror(
            "Error",
            "Enter valid integer"
        )

        return

    current_n = n

    solutions = solve_n_queens(n)

    current_index = 0

    show_solution()


# ---------------- DISPLAY SOLUTION ---------------- #

def show_solution():

    if not solutions:
        return

    draw_board(
        canvas,
        solutions[current_index],
        current_n
    )

    result_label.config(
        text=f"Solution {current_index + 1} of {len(solutions)}"
    )


# ---------------- NEXT BUTTON ---------------- #

def next_solution():

    global current_index

    if not solutions:
        return

    if current_index < len(solutions) - 1:

        current_index += 1

        show_solution()


# ---------------- PREVIOUS BUTTON ---------------- #

def previous_solution():

    global current_index

    if not solutions:
        return

    if current_index > 0:

        current_index -= 1

        show_solution()


# ---------------- GUI WINDOW ---------------- #

root = tk.Tk()

root.title("N Queen Solver")

root.geometry("800x850")


# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="N Queen Solver",
    font=("Arial", 24)
)

title.pack(pady=10)


# ---------------- ENTRY ---------------- #

entry = tk.Entry(
    root,
    font=("Arial", 14)
)

entry.pack(pady=5)


# ---------------- SOLVE BUTTON ---------------- #

solve_button = tk.Button(
    root,
    text="Solve",
    font=("Arial", 12),
    command=start_solver
)

solve_button.pack(pady=10)


# ---------------- RESULT LABEL ---------------- #

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14)
)

result_label.pack(pady=5)


# ---------------- CONTROL BUTTONS ---------------- #

button_frame = tk.Frame(root)

button_frame.pack(pady=10)

prev_button = tk.Button(
    button_frame,
    text="Previous",
    width=12,
    command=previous_solution
)

prev_button.grid(row=0, column=0, padx=10)

next_button = tk.Button(
    button_frame,
    text="Next",
    width=12,
    command=next_solution
)

next_button.grid(row=0, column=1, padx=10)


# ---------------- CANVAS ---------------- #

canvas = tk.Canvas(
    root,
    width=700,
    height=700
)

canvas.pack()


# ---------------- RUN ---------------- #

root.mainloop()