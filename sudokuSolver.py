from typing import List
from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows_dict = {}
        for i in range(len(board)):
            rows_dict[i] = [int(x) for x in board[i] if x != '.']
        cols_dict = {}
        for i in range(len(board)):
            x = [board[j][i] for j in range(len(board))] 
            cols_dict[i] = [int(x) for x in x if x != '.']
            
        boxes_dict = {}
        for i in range(0,9,3):
            for j in range(0,9,3):
                #list containing all the values in the 3x3 box
                box = []
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        box.append(board[k][l])
                boxes_dict[(i//3,j//3)] = [int(x) for x in box if x != '.']
        print('----')
        def availableNumbers(row, col):
            #returns a list of available numbers for a given row and column
            available = []
            for i in range(1,10):
                if i not in rows_dict[row] and i not in cols_dict[col] and i not in boxes_dict[(row//3,col//3)]:
                    available.append(i)
                    rows_dict[row].append(i)
                    cols_dict[col].append(i)
                    boxes_dict[(row//3,col//3)].append(i)
            return available
        def removeNumber(row, col, number):
            #check if string number is a valid number
            if number not in ['1','2','3','4','5','6','7','8','9']:
                return 
            number = int(number)
            #removes a number from the row, column and box
            rows_dict[row].remove(number)
            cols_dict[col].remove(number)
            boxes_dict[(row//3,col//3)].remove(number)
        
        def backtrack(row, col):
            #backtracking function
            if col == len(board):
                col = 0
                row += 1
            if row == len(board):
                return True
            if board[row][col] == '.':
                for i in availableNumbers(row, col):
                    board[row][col] = str(i)
                    if backtrack(row, col+1):
                        return True
                    removeNumber(row, col, board[row][col])
                    board[row][col] = '.'
                return False
            else:
                return backtrack(row, col+1)
        backtrack(0,0)
                
            

def printSudokuBoard(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

printSudokuBoard(board)

s = Solution()
s.solveSudoku(board)
printSudokuBoard(board)
