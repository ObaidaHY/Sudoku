import random
from copy import deepcopy

firstBoard = [
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]
     ]


def findEmpty(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                return y, x  # y = row , x = column
    # if we got here it mean that we finish the sudoku, so return none
    return None


def validCheck(board, number, coordinates):
    # checking row
    for x in range(len(board[0])):
        if number == board[coordinates[0]][x] and coordinates[1] != x:  # coordinates[0]= row
            return False

    # checking column
    for y in range(len(board)):
        if number == board[y][coordinates[1]] and coordinates[0] != y:
            return False

    # checking the box
    box_x = coordinates[1] // 3
    box_y = coordinates[0] // 3

    for y in range(box_y * 3, box_y * 3 + 3):
        for x in range(box_x * 3, box_x * 3 + 3):
            if number == board[y][x] and (y, x) != coordinates:
                return False

    return True


def generateRandomBoard():
    # end condition:- getting to the end of the board - the function findEmpty return NONE
    find = findEmpty(firstBoard)
    if find is None:  
        return True
    else:
        row, col = find
    for number in range(1, 10):
        randomNumber = random.randint(1, 9)  
        if validCheck(firstBoard, randomNumber, (row, col)):
            firstBoard[row][col] = randomNumber
            if generateRandomBoard():
                return True

            firstBoard[row][col] = 0
    return False


def deleteCells(firstBoard,number):
    while number:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if firstBoard[row][col] != 0:
            firstBoard[row][col] = 0
            number = number - 1


def sudokuGenerate(level):

    
    generateRandomBoard()
    if level == 1:
        deleteCells(firstBoard,30)
    if level == 2:
        deleteCells(firstBoard,40)
    if level == 3:
        deleteCells(firstBoard,50)

    return firstBoard





        
