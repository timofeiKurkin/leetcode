from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def run(node: Optional[TreeNode], max_node: int) -> int:
            if not node:
                return 0

            isGood = 1 if max_node <= node.val else 0
            max_node = node.val

            return isGood + run(node.left, max_node) + run(node.right, max_node)

        return run(root, 0)
