from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isValid(board: List[List[str]], row, col, visited: set((int,int))):
            if row < 0 or row > len(board) -1:
                return False
            if col < 0 or col > len(board[0]) -1:
                return False
            if (row,col) in visited:
                return False
            return True

        def searchWord(board: List[List[str]], row: int, colum: int, word: str, target_word:str, visited:set((int,int))):
            if not isValid(board, row, colum, visited):
                return ''
            word += board[row][colum]         
            if board[row][colum] != target_word[0]:
                return ''
            visited.add((row,colum))
            target_word = target_word[1:]
            if len(target_word) == 0:
                return word
            result = searchWord(board, row+1, colum, word, target_word, visited)
            if result != '':
                return result
            result = searchWord(board, row-1, colum, word, target_word, visited)
            if result != '':
                return result
            result = searchWord(board, row, colum+1, word, target_word, visited)
            if result != '':
                return result
            result = searchWord(board, row, colum-1, word, target_word, visited)
            if result != '':
                return result
            visited.remove((row,colum))
            return ''
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                visited = set()
                result = searchWord(board, row, col, '', word, visited)
                if result != '':
                    return True
        return False

                
s = Solution()
board = [["a","b"],["c","d"]]
word = "cdba"
print(s.exist(board, word))
board = [["A"]]
word = "A"
print(s.exist(board, word))

board = [["A"]]
word = "B"
print(s.exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(s.exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(s.exist(board, word))

