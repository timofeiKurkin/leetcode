from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional["TreeNode"],
        p: "TreeNode",
        q: "TreeNode",
    ) -> Optional["TreeNode"]:
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)

        if leftLCA and rightLCA:
            return root

        return leftLCA or rightLCA
