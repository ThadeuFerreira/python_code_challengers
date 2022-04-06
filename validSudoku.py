from typing import List

class Solution:
    def isValidRow(row):
            row = [i for i in row if i != '.']
            return len(set(row)) == len(row)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for row in board:
            if not self.isValidRow(row):
                return False
        #check columns
        for i in range(len(board)):
            column = []
            for j in range(len(board)):
                column.append(board[j][i])
            if not self.isValidRow(column):
                return False
        #check 3x3 boxes
        for i in range(0,9,3):
            for j in range(0,9,3):
                box = []
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        box.append(board[k][l])
                if not self.isValidRow(box):
                    return False
        return True


s = Solution()


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(s.isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(s.isValidSudoku(board))