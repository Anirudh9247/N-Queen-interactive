def draw_board(canvas, solution, n):
    canvas.delete("all")

    canvas_width = int(canvas['width'])
    canvas_height = int(canvas['height'])
    
    padding = 20
    board_size = min(canvas_width, canvas_height) - 2 * padding
    cell_size = board_size / n
    
    x_offset = (canvas_width - board_size) / 2
    y_offset = (canvas_height - board_size) / 2

    light_color = "#EEEED2"
    dark_color = "#769656"

    font_size = int(cell_size * 0.6)

    for row in range(n):
        for col in range(n):
            x1 = x_offset + col * cell_size
            y1 = y_offset + row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            color = light_color if (row + col) % 2 == 0 else dark_color

            canvas.create_rectangle(
                x1, y1, x2, y2,
                fill=color, outline="black"
            )

            if solution[row] == col:
                canvas.create_text(
                    x1 + cell_size / 2,
                    y1 + cell_size / 2,
                    text="♛",
                    font=("Arial", font_size),
                    fill="black"
                )