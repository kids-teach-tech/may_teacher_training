from sudokuLibBasic import display_sudoku, sudokus

def sudokuCoordinates(coords):
    return [int(coords[0]), int(coords[2])]

def is_valid_move(sudoku, row, col, num):
    # Check if 'num' is already present in the row and column
    for i in range(9):
        if sudoku[row][i] == num:
            return False
        if sudoku[i][column] == num:
            return False

    # Check if 'num' is already present in the 3x3 grid
    """
    YOU MANY OPTIONS HERE TO FIND THE STARTING ROW AND COLUMN OF THE 3X3 GRID:

    1.
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    2.
    if (row == 0 or row == 1 or row == 2):
        start_row = 0
    elif (row == 3 or row == 4 or row == 5):
        start_row = 3
    elif (row == 6 or row == 7 or row == 8):
        start_row = 6

    if (column == 0 or column == 1 or column == 2):
        start_column = 0
    elif (column == 3 or column == 4 or column == 5):
        start_column = 3
    elif (column == 6 or column == 7 or column == 8):
        start_column = 6

    3. (The one I chose)
    indexToStart = [0, 0, 0, 3, 3, 3, 6, 6, 6]
    start_column = indexToStart[column]
    start_row = indexToStart[row]
    """

    indexToStart = [0, 0, 0, 3, 3, 3, 6, 6, 6]
    start_column = indexToStart[col]
    start_row = indexToStart[row]

    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False

    return True

sudoku = sudokus[0]

while True:
    display_sudoku(sudoku)

    num = int(input("What number would you like to place?: "))
    position = sudokuCoordinates(input("Where would you like to place it? [X,Y]: "))
    
    if is_valid_move(sudoku, position[0], position[1], num):
        sudoku[position[0]][position[1]] = num
    else:
        print("\nThat was not a valid move, make another!\n")