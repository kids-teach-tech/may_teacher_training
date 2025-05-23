# Student reference: https://docs.google.com/document/d/1k98cnkeHV0ICjOMLOBIEqHxkRgRKUaVqte_5iSDNctQ/preview?usp=sharing

from sudokuLibAdvanced import display_sudoku, find_empty_cell, remove_cells, 
from random import shuffle

def sudokuCoordinates(coords):
    return [int(coords[0]), int(coords[2])]

def is_valid_move(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return False
        if sudoku[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False
    return True

def generate_sudoku(): # CREATE THIS FUNCTION --------------------------------------------------
    # Generate a new Sudoku puzzle by solving an empty sudoku, this only works if you randomly choose the order solve_sudoku() guesses
    # Then remove numbers from the solved sudoku (In student reference)
    return True # Placeholder
    
def solve_sudoku(sudoku): # CREATE THIS FUNCTION -----------------------------------------------
    # Find an empty cell in the Sudoku

    # If all cells are filled, the Sudoku is solved

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(numbers)

    # Loop over these numbers and check it they are valid in the empty cell
    for i in range(9):
        current_guess = numbers[i]
    
    return False

sudoku = generate_sudoku()

while (True):
    display_sudoku(sudoku)

    num = int(input("What number would you like to place?: "))
    position = sudokuCoordinates(input("Where woudld you like to place it? [X,Y]: "))
    
    if is_valid_move(sudoku, position[0], position[1], num):
        sudoku[position[0]][position[1]] = num
    else:
        print("\nThat was not a valid move, make another!\n")