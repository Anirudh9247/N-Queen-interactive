with open('main.py', 'r') as f:
    content = f.read()

old = """    solutions = solve_n_queens(n)

    if solutions:

        draw_board(
            canvas,
            solutions[0],
            n
        )

        result_label.config(
            text=f"Total Solutions: {len(solutions)}"
        )"""

new = """    solutions = solve_n_queens(n)

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

        result_label.config(text=f"No solutions found for n={n}")"""

content = content.replace(old, new)

with open('main.py', 'w') as f:
    f.write(content)