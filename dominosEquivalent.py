# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

# Example 1:

# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# Example 2:

# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3

from typing import List
from collections import Counter
import math
def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    
    l = []
    for i in dominoes:
        max_i = max(i[0], i[1])
        min_i = min(i[0], i[1])
        l.append((max_i,min_i))
    
    s = Counter(l)
        
    count = 0
    for k, v in s.items():
        if v > 1:
            if v == 1:
                count += 1
                continue
            count += math.factorial(v)/(2*math.factorial(v-2))
    return count

d = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(numEquivDominoPairs(d))
dominoe = [[1,2],[2,1],[3,4],[5,6]]
print(numEquivDominoPairs(dominoe))