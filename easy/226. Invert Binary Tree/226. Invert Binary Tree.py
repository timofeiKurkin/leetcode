from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.left or root.right:
            root = TreeNode(root.val, root.right, root.left)
        
        root = TreeNode(
            root.val, self.invertTree(root.left), self.invertTree(root.right)
        )
        
        return root
