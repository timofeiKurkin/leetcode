from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return

        head = preorder.pop(0)
        position = inorder.index(head)

        left = self.buildTree(preorder, inorder[:position])
        right = self.buildTree(preorder, inorder[position + 1 :])

        return TreeNode(val=head, left=left, right=right)


solution = Solution()
print(solution.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
print(solution.buildTree(preorder=[-1], inorder=[-1]))
