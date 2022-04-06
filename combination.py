from typing import List

def combination(N: List, K : int) -> List[List[int]]:
    if K == 0:
        return [[]]
    if K == 1:
        return [[i] for i in N]
    if K == len(N):
        return [N]
    if K > len(N):
        return []
    result = []
    for i in range(len(N)):
        k = combination(N[i+1:], K-1)
        for j in k:
            result.append([N[i]] + j)
    return result

print(combination([1,2,3,4,5,6,7,8,9,10], 4))
