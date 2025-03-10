from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return

        head = postorder.pop()
        position = inorder.index(head)

        right_tree = self.buildTree(inorder[position + 1 :], postorder)

        left_tree = self.buildTree(inorder[:position], postorder)

        return TreeNode(val=head, right=right_tree, left=left_tree)
