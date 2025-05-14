from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

    def updateNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        min_node = self.findMin(root.right)
        root.val = min_node.val
        root.right = self.deleteNode(root.right, min_node.val)

        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def run(lief: Optional[TreeNode], key: int) -> Tuple[bool, Optional[TreeNode]]:
            if not lief:
                return False, None

            if lief.val == key:
                return True, self.updateNode(lief)

            right = run(lief.right, key)

            if right[0]:
                lief.right = right[1]
                return True, lief
            else:
                lief.left = run(lief.left, key)[1]
                return False, lief

        return run(root, key)[1]
