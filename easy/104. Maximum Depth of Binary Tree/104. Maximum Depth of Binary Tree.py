from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def Run(curr: TreeNode, deep_index: int):
        #     if not curr:
        #         return 0
        #     if not curr.left and not curr.right:
        #         return deep_index
        #     return max(Run(curr.left, deep_index + 1), Run(curr.right, deep_index + 1))
        # deep: int = Run(root, 1)
        # return deep

        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
