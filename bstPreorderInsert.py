# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

# It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

# A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

# A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, start, end):
            if start > end:
                return None
            root = TreeNode(preorder[start])
            i = start + 1
            while i <= end and preorder[i] < root.val:
                i += 1
            root.left = dfs(preorder, start + 1, i - 1)
            root.right = dfs(preorder, i, end)
            return root
        return dfs(preorder, 0, len(preorder) - 1)

    def printTree(self, root: Optional[TreeNode]):
        def dfs(root):
            if root is None:
                return
            print(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)

s = Solution()
preorder = [8,5,1,7,10,12]
r = s.bstFromPreorder(preorder)
s.printTree(r)
