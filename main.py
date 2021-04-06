# This is the main file for Sudoku solver program
# Reference: https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/

# Blocks
# 1. Read input (default assuming "png" file)           --- Not finished
# 2. Distinguish digits (MNIST model)                   --- Not finished
# 3. !Main! Algorithm to solve the Sudoku board         --- Done
# 4. Other utilities (print board / find empty ...)     --- Done


print("Hello 'Sudoku' !!")

VERBOSE = False


# If 9 numbers in the grid & column/row valid
def valid(board, num, pos):
    """
    num: num (1 ~ 9) for the answer
    pos: (col, row) in the board
    box: index of the box (from 1 - 9) top-left == 1, bottom-right = 9
    """
    x, y = pos[0], pos[1]

    # Check Row
    for i in range(len(board[0])):
        if board[x][i] == num and y != i:
            return False

    # Check Column
    for i in range(len(board)):
        if board[i][y] == num and x != i:
            return False

    # Check box
    box_x = y // 3
    box_y = x // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != (x, y):
                return False
    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None


def solve(board):
    find = find_empty(board)

    if not find:
        return True
    else:
        x, y = find
    for i in range(1, 10):
        if valid(board, i, (x, y)):
            board[x][y] = i

            if VERBOSE:
                print("Current position: ", find)
                print_board(board)

            if solve(board):  # Recursively solve the board
                return True

            board[x][y] = 0  # Reset the empty to zero
    return False


# Print board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("---------------------------")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" |", end="")  # keep print at "same" line
            num = board[i][j]
            if j == 8:
                print("{:2d} |".format(num))
            else:
                print("{:2d}".format(num), end="")
    # Print at last line
    print("---------------------------")


# Test Board

test_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

print("Input Board:")
print_board(test_board)

ans = solve(test_board)
print("Got an answer: ", ans)
if ans:
    print("Solution Board")
    print_board(test_board)
else:
    print("Not found solution!")
