from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def run(tree: Optional[TreeNode]):
            nonlocal diameter
            if not tree:
                return 0
            if not tree.left and not tree.right:
                return 1
            
            left = run(tree.left)
            right = run(tree.right)
            
            max_depth = max(left, right)
            diameter = max(diameter, left + right)
            return max_depth

        run(root)

        return diameter
