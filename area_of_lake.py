from typing import List

def print_matrix(matrix: List[List[int]]):
    for row in matrix:
        print(row)
    print("-"*len(matrix[0]*4))

#for each point in the matrix, check the neighbours on the top, down, left and right
#mark with -1 when a point with water is visited
#sum the result of each travel
def depth_first_search(matrix: List[List[int]], row, col) -> List[int]:
    if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]) and matrix[row][col] == 1:
        matrix[row][col] = -1
        right = depth_first_search(matrix, row, col + 1)
        down = depth_first_search(matrix, row + 1, col)
        left = depth_first_search(matrix, row, col - 1)
        up = depth_first_search(matrix, row - 1, col)
        return right + down + left + up + 1
    return 0 

#a lake is a large area of water, surrounded by land.
#the water is represented by 1 and land is represented by 0.
#water is connected only vertically or horizontally, not diagonally.
#calculate the areas of all the lakes in the given 2D array.
def lake_areas(matrix: List[List[int]]) -> List[int]:
    sizes = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                sizes.append(depth_first_search(matrix, row, col))
    return sizes

matrix = [
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

print(lake_areas(matrix))
print(matrix)
matrix = [
    [1, 1, 1, 1, 1]*5
]
print(lake_areas(matrix))
print(matrix)