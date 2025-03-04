from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if not root:
        #     return float("inf")
        # if not k:
        #     return root.val
        # return min(
        #     self.kthSmallest(
        #         root.left,
        #         k - 1,
        #     ),
        #     self.kthSmallest(root.right, k - 1),
        # )

        def run(tree: Optional[TreeNode]) -> List[int]:
            if not tree:
                return []
            
            return run(tree.left) + [tree.val] + run(tree.right)

        return run(root)[k - 1]
