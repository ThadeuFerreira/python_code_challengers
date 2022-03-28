# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #create minimum triangle
        #that has the same dimensions as the input triangle
        min_triangle = [[0]*len(row) for row in triangle]

        height = len(triangle) -1
        #Goin from bottom to top
        #for each row, find the minimum path sum from the row above
        min_triangle[height] = triangle[height]
        for i in reversed(range(height)):
            for j in range(len(triangle[i])):
                min_triangle[i][j] = min(min_triangle[i+1][j], min_triangle[i+1][j+1]) + triangle[i][j]
        #return the minimum path sum from the top
        return min_triangle[0][0]

    #print triangle
    def print_triangle(self, triangle: List[List[int]]):
        height = len(triangle)
        for i in range(height):
            spaces = " "*(height - i - 1)
            print(spaces, end="")
            for j in range(len(triangle[i])):
                print(triangle[i][j], end=" ")
            print()

s = Solution()

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
s.print_triangle(triangle)
s.minimumTotal(triangle=triangle)
triangle = [[2],[3,4],[6,5,7],[4,1,8,3],[4,1,8,3,1]]
s.minimumTotal(triangle=triangle)
s.print_triangle(triangle)
triangle = [[-10]]
s.minimumTotal(triangle=triangle)
