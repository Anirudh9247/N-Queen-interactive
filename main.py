import tkinter as tk
from tkinter import messagebox

from solver import solve_n_queens
from board import draw_board


def start_solver():

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

    solutions = solve_n_queens(n)

    if solutions:

        canvas.delete("all")

        draw_board(
            canvas,
            solutions[0],
            n
        )

        result_label.config(
            text=f"Total Solutions: {len(solutions)}"
        )

    else:

        canvas.delete("all")

        result_label.config(text=f"No solutions found for n={n}")


# ---------------- WINDOW ---------------- #

root = tk.Tk()

root.title("N Queen Solver")

root.geometry("800x800")

title = tk.Label(
    root,
    text="N Queen Solver",
    font=("Arial", 22)
)

title.pack(pady=10)

entry = tk.Entry(
    root,
    font=("Arial", 14)
)

entry.pack(pady=5)

solve_button = tk.Button(
    root,
    text="Solve",
    font=("Arial", 12),
    command=start_solver
)

solve_button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14)
)

result_label.pack()

canvas = tk.Canvas(
    root,
    width=700,
    height=700
)

canvas.pack()

root.mainloop()

