# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
from typing import Optional
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        def addS(root):
            if root is None:
                return 
            s.add(k - root.val)
            addS(root.left)
            addS(root.right)
        addS(root)
        
        def dfs(root):
            if root is None:
                return False
            if root.val in s:
                return True
            
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)
s = Solution()
root = TreeNode(1)
print(s.findTarget(root, 2))

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)


print(s.findTarget(root, 9))