from typing import List

def rotate(matrix: List[List[int]]) ->  None:
    #transpose in place
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    #reflect in place
    for i in range(len(matrix)):
        for j in range(len(matrix[0])//2):
            matrix[i][j], matrix[i][len(matrix[0])-1-j] = matrix[i][len(matrix[0])-1-j], matrix[i][j]



def assert_equal_matrix(matrix1: List[List[int]], matrix2: List[List[int]]) -> None:
    assert len(matrix1) == len(matrix2)
    for i in range(len(matrix1)):
        assert len(matrix1[i]) == len(matrix2[i])
        for j in range(len(matrix1[i])):
            assert matrix1[i][j] == matrix2[i][j]

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# output = [[7,4,1],[8,5,2],[9,6,3]]
# result = rotate(matrix)
# assert_equal_matrix(result, output)

# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# result = rotate(matrix)
# assert_equal_matrix(result, output)

def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    s = {}
    for i in dominoes:
        max_i = max(i[0], i[1])
        min_i = min(i[0], i[1])
        if (max_i,min_i) in s:
            s[(max_i,min_i)] += 1
            continue
        
        s[(max_i,min_i)] = 0
        
    pairs = 0
    count = 0
    for k, v in s:
        if v > 0:
            pairs += v * (v - 1) // 2
            count += v
    return pairs + count * (count - 1) // 2
