from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result: List[List[int]] = []

        def run(tree: Optional[TreeNode], target: int, curr_path: List[int]):
            if not tree:
                return

            curr_path.append(tree.val)

            if not tree.left and not tree.right and target == tree.val:
                result.append([*curr_path])

            run(tree.left, target - tree.val, curr_path)
            run(tree.right, target - tree.val, curr_path)

            curr_path.pop()

        run(root, targetSum, [])

        return result
