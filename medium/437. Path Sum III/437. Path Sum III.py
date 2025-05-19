from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        # self.res = 0
        # def dfs(node: Optional[TreeNode], remind: int) -> None:
        #     if node is None:
        #         return
        #     new_remind = remind - node.val
        #     if new_remind == 0:
        #         self.res += 1
        #     dfs(node.left, new_remind)
        #     dfs(node.right, new_remind)
        # def run(node: Optional[TreeNode]) -> None:
        #     if node is None:
        #         return
        #     dfs(node, targetSum)
        #     run(node.left)
        #     run(node.right)
        # run(root)
        # return self.res

        def countPathsFrom(node: Optional[TreeNode], curr_sum: int) -> int:
            if node is None:
                return 0

            curr_sum += node.val
            match = 1 if curr_sum == targetSum else 0

            return (
                match
                + countPathsFrom(node.left, curr_sum)
                + countPathsFrom(node.right, curr_sum)
            )

        return (
            countPathsFrom(root, 0)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )
