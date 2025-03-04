from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if prev is not None and cur.val <= prev:
                return False

            prev = cur.val
            cur = cur.right

        return True

        # def run(tree: Optional[TreeNode]) -> List[int]:
        #     if not tree:
        #         return []
        #     return run(tree.left) + [tree.val] + run(tree.right)
        # items = run(root)
        # for i in range(1, len(items)):
        #     if items[i] <= items[i - 1]:
        #         return False
        # return True
