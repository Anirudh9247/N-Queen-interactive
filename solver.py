def solve_n_queens(n):
    solutions = []
    board = [["."] * n for _ in range(n)]
    
    cols = [False] * n
    pos_diag = [False] * (2 * n - 1)  # row + col
    neg_diag = [False] * (2 * n - 1)  # row - col + (n - 1)
    
    def backtrack(row):
        if row == n:
            solutions.append(["".join(r) for r in board])
            return
            
        for col in range(n):
            if cols[col] or pos_diag[row + col] or neg_diag[row - col + n - 1]:
                continue
                
            cols[col] = pos_diag[row + col] = neg_diag[row - col + n - 1] = True
            board[row][col] = "Q"
            
            backtrack(row + 1)
            
            cols[col] = pos_diag[row + col] = neg_diag[row - col + n - 1] = False
            board[row][col] = "."
            
    backtrack(0)
    return solutions