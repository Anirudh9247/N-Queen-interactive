def create_board(n):
    board= [["."for _ in range(n)]for _ in range(n)]
    return board
def is_safe(board,row,col,n):
    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # check upper left diagonal
    i,j = row,col-1
    while i>=0 and j>=0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    #check upper right diagonal
    i,j = row,col+1
    while i>=0 and j<n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
    
    return True


def solve(board, row, n, solutions):

    # Base Case → All queens placed
    if row == n:
        solutions.append(["".join(r) for r in board])
        return

    # Try placing queen in every column
    for col in range(n):

        if is_safe(board, row, col, n):
            board[row][col] = "Q"

            # Recurse for next row
            solve(board, row + 1, n, solutions)

            # Backtrack
            board[row][col] = "."

def solve_n_queens(n):
    board = create_board(n)
    solutions = []
    solve(board, 0, n, solutions)
    return solutions