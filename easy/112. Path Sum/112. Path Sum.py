# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def Run(root, target):
            if not root:
                return False

            if not root.left and not root.right:
                return target - root.val == 0

            return Run(root.left, target) and Run(root.right, target)

        return Run(root, targetSum)
