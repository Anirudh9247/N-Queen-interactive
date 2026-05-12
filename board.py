import tkinter as tk
from tkinter import messagebox

# ---------------- SOLVER ---------------- #

def is_safe(board, row, col, n):

    for i in range(row):
        if board[i] == col:
            return False

    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row, n, solutions):

    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row] = col

            solve(board, row + 1, n, solutions)

            board[row] = -1


def solve_n_queens(n):

    board = [-1] * n
    solutions = []

    solve(board, 0, n, solutions)

    return solutions

# ---------------- GUI ---------------- #

def start_solver():

    canvas.delete("all")

    try:
        n = int(entry.get())

        if n < 4:
            messagebox.showerror("Error", "N must be >= 4")
            return

    except:
        messagebox.showerror("Error", "Enter valid integer")
        return

    solutions = solve_n_queens(n)

    draw_board(solutions[0], n)

    result_label.config(
        text=f"Total Solutions: {len(solutions)}"
    )


def draw_board(solution, n):

    size = 50

    for row in range(n):

        for col in range(n):

            x1 = col * size
            y1 = row * size

            x2 = x1 + size
            y2 = y1 + size

            color = "white" if (row + col) % 2 == 0 else "gray"

            canvas.create_rectangle(
                x1, y1, x2, y2,
                fill=color
            )

            if solution[row] == col:

                canvas.create_text(
                    x1 + 25,
                    y1 + 25,
                    text="♛",
                    font=("Arial", 24)
                )

# ---------------- WINDOW ---------------- #

root = tk.Tk()

root.title("N Queen Solver")

root.geometry("700x700")

title = tk.Label(
    root,
    text="N Queen Solver",
    font=("Arial", 20)
)

title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

solve_button = tk.Button(
    root,
    text="Solve",
    command=start_solver
)

solve_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

canvas = tk.Canvas(
    root,
    width=600,
    height=600
)

canvas.pack()

root.mainloop()