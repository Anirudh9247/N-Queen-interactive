def draw_board(canvas, solution, n):

    canvas.delete("all")

    size = 60

    for row in range(n):

        for col in range(n):

            x1 = col * size
            y1 = row * size

            x2 = x1 + size
            y2 = y1 + size

            color = "white" if (row + col) % 2 == 0 else "gray"

            canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill=color
            )

            if solution[row] == col:

                canvas.create_text(
                    x1 + 30,
                    y1 + 30,
                    text="♛",
                    font=("Arial", 28)
                )