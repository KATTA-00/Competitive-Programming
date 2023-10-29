def is_safe(board, row, col):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check the lower left diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve(board, col):
    if col == len(board):
        return 1

    count = 0
    for i in range(len(board)):
        if board[i][col] == '.' and is_safe(board, i, col):
            board[i][col] = 'Q'
            count += solve(board, col + 1)
            board[i][col] = '.'

    return count


board = [list(input()) for _ in range(8)]
total_ways = solve(board, 0)
print(total_ways)


