from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_path = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            if not root.left and not root.right:
                return root.val

            left_tree = max(dfs(root.left), 0)
            right_tree = max(dfs(root.right), 0)

            curr_sum = root.val + left_tree + right_tree

            self.max_path = max(self.max_path, curr_sum)

            return root.val + max(left_tree, right_tree)

        dfs(root)
        return self.max_path


solution = Solution()
# print(solution.maxPathSum([1,2,3]))
# print(solution.maxPathSum())
# print(solution.maxPathSum([-3]))
