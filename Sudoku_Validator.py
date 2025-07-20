def is_valid_sudoku(board):
    def is_valid_block(block):
        nums = [num for num in block if num != 0]
        return len(nums) == len(set(nums))

    # Check rows
    for row in board:
        if not is_valid_block(row):
            return False

    # Check columns
    for col in zip(*board):
        if not is_valid_block(col):
            return False

    # Check 3x3 subgrids
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            block = [
                board[i][j]
                for i in range(box_row, box_row + 3)
                for j in range(box_col, box_col + 3)
            ]
            if not is_valid_block(block):
                return False

    return True

print("Enter the Sudoku board row by row (9 numbers per row, use 0 for empty cells):")
board = []
for i in range(9):
    row = list(map(int, input(f"Row {i+1}: ").strip().split()))
    if len(row) != 9:
        print("Invalid input. Each row must have 9 numbers.")
        exit()
    board.append(row)

if is_valid_sudoku(board):
    print("The Sudoku board is VALID.")
else:
    print("The Sudoku board is INVALID.")
