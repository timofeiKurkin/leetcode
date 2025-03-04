from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # def run(tree: Optional[TreeNode]) -> List[int]:
        #     if not tree:
        #         return []
        #     return run(tree.left) + [tree.val] + run(tree.right)
        # array = run(root)[1:]
        # current = root
        # while len(array):
        #     if current.left:
        #         current.left = None
        #     current.right = TreeNode(val=array.pop(0))
        #     current = current.right

        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        right_subtree = root.right

        root.right = root.left
        root.left = None

        curr = root
        while curr.right:
            curr = curr.right

        curr.right = right_subtree
