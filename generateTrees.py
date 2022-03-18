from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        #base case: when 0 node is involved, tree is None
        c = [[[None]] * (n+1)]
        #i is number of nodes
        for i in range(1, n+1):
            c.append([])
            #j is which number to start BST
            for j in range(1, n+2-i):
                c[i].append([])
                #k is the root
                for k in range(j, j+i):
					#go through every combination of left and right subtrees
                    for left in c[k-j][j-1]:
                        for right in c[j+i-k-1][k]:
                            c[i][j-1].append(TreeNode(k, left, right))
            c[i].append([None])
        return c[n][0]

s = Solution()
print(len(s.generateTrees(11)))
        