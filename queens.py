from typing import List, Optional

class Bord:
    def __init__(self, rows=8, cols=8) -> None:
        self.cols = cols
        self.rows = rows
        self.bord = [[0] * cols for _ in range(rows)]

    def flipPositionValue(self, row: int, col: int) -> None:
        self.bord[col][row] = 1 - self.bord[col][row]

    def isValidPosition(self, row: int, col: int) -> bool:
        return 0 <= row < self.cols and 0 <= col < self.rows

    def checkDiagonals(self, row: int, col: int) -> bool:
        for c in range(self.cols):
            if self.bord[c][row] == 1:
                return False
        for r in range(self.rows):
            if self.bord[col][r] == 1:
                return False
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.bord[c][r] == 1:
                return False
        for r, c in zip(range(row, self.rows, 1), range(col, self.cols, 1)):
            if self.bord[c][r] == 1:
                return False
        return True
    
    def isPositionAvailable(self, row: int, col: int) -> bool:
        for r in range(self.rows):
            if self.bord[row][r] == 1:
                return False
        for c in range(self.cols):
            if self.bord[c][col] == 1:
                return False
        return self.checkDiagonals(row, col)
            
    def addQueen(self, row: int, col: int) -> bool:
        if not self.isPositionAvailable(row, col):
            return False
        self.bord[col][row] = 1
        return True

    def solveQuens(self, n: int) -> bool:
        printBoard(self)
        print("---"*50)
        if n == 0:
            return True
        for r in range(self.rows):
            for c in range(self.cols):
                if self.addQueen(r, c):
                    if self.solveQuens(n-1):
                        return True
                    self.flipPositionValue(r, c)
        return False
        

def printBoard(bord: Bord) -> None:
    for row in bord.bord:
        print(row)
    


b = Bord(8,8)
printBoard(b)
print(b.solveQuens(8))
printBoard(b)