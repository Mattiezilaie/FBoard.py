# Author: Mahtab Zilaie
# Date: 11 25 2019
# Description:A class named FBoard for playing a game, where player x is trying to get
# her piece to row 7 and player o is trying to make it so player x doesn't have any legal moves.
# An 8x8 list of lists for tracking what's on each square of the board.A data member for tracking
# the game state, that holds one of the following string values.Data members to keep track of where
# the x piece is.

class FBoard:
    """class to initialize the board"""
    def __init__(self):
        self.__board = [['-' for i in range(8)] for j in range(8)]
        self.__board[7][0] = 'o'
        self.__board[7][2] = 'o'
        self.__board[7][4] = 'o'
        self.__board[7][6] = 'o'
        self.__gameState = "UNFINISHED"
        self.__XRow = 0
        self.__XCol = 3
        self.__board[0][3] = 'x'

    def get_game_state(self):
        return self.__gameState

    def move_x(self, row, col):
        if self.__gameState == "UNFINISHED":
            if (row >= 0 and row < 8 and col >= 0 and col < 8):
                if (((self.__XRow - 1) == row and (self.__XCol - 1 == col)) or (
                        (self.__XRow + 1) == row and (self.__XCol - 1) == col) or (
                        (self.__XRow - 1) == row and (self.__XCol + 1) == col) or (
                        (self.__XRow + 1) == row and (self.__XCol + 1) == col)):
                    if self.__board[row][col] == '-':
                        self.__board[row][col] = 'x'
                        self.__board[self.__XRow][self.__XCol] = '-'
                        self.__XRow = row
                        self.__XCol = col
                    if self.__XRow == 7:
                        self.__gameState = "X_WON"
                        return True
                    else:
                        return False

                return False

            return False

        return False

    def move_o(self, fromRow, fromCol, toRow, toCol):
        if self.__gameState == "UNFINISHED":
            if (fromRow >= 0 and fromRow < 8 and fromCol >= 0 and fromCol < 8 and toRow >= 0 and toRow < 8 and toCol >= 0 and toCol < 8):
                if self.__board[fromRow][fromCol] == 'o':
                    if self.__board[toRow][toCol] == '-':
                        if fromRow - 1 == toRow:
                            if (((fromCol - 1) == toCol) or ((fromCol + 1) == toCol)):
                                self.__board[fromRow][fromCol] = '-'
                                self.__board[toRow][toCol] = 'o'
                                if ((self.__board[self.__XRow - 1][self.__XCol - 1] == 'o') and (
                                        self.__board[self.__XRow - 1][self.__XCol + 1] == 'o') and (
                                        self.__board[self.__XRow + 1][self.__XCol - 1] == 'o') and (
                                        self.__board[self.__XRow + 1][self.__XCol + 1] == 'o')):
                                    self.__gameState = 'O_WON'
                                    return True
                                else:
                                    return False
                            return False
                        return False
                    return False
                return False
            return False
    def print_board(self):
        for i in range(len(self.__board)):
            print(self.__board[i])
            print('')




