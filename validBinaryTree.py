# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        def validate(root, maxLimit, minLimit):
            if root is None:
                return True
            if root.val < minLimit or root.val > maxLimit:
                return False
            
            return validate(root.left, root.val, minLimit) and validate(root.right, maxLimit, root.val)
            
        maxLimit = math.inf
        minLimit = -math.inf
        return validate(root, maxLimit, minLimit)

s = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

s.isValidBST(root)