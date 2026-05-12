def is_safe(board, row, col):

    for i in range(row):

        # same column
        if board[i] == col:
            return False

        # diagonal check
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row, n, solutions):

    # all queens placed
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):

        if is_safe(board, row, col):

            board[row] = col

            solve(board, row + 1, n, solutions)

            # backtrack
            board[row] = -1


def solve_n_queens(n):

    board = [-1] * n

    solutions = []

    solve(board, 0, n, solutions)

    return solutions