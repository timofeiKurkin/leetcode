from typing import Literal, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # 1 is the right direction
        # -1 is the left direction
        def dfs(node: Optional[TreeNode], path: int, direction: Literal[1, -1]) -> int:
            if not node:
                return path

            if not node.left and not node.right:
                return path + 1

            if direction == 1:
                return max(dfs(node.left, path + 1, -1), dfs(node.right, 0, 1))
            else:
                return max(dfs(node.right, path + 1, 1), dfs(node.left, 0, -1))

        return max(dfs(root.left, 0, -1), dfs(root.right, 0, 1))
