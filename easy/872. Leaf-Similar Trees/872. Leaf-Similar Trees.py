from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], leaf_list: List[int]) -> None:
            if root:
                if not root.left and not root.right:
                    leaf_list.append(root.val)
                dfs(root.left, leaf_list)
                dfs(root.right, leaf_list)

        list1 = []
        list2 = []

        dfs(root1, list1)
        dfs(root2, list2)

        return list1 == list2
