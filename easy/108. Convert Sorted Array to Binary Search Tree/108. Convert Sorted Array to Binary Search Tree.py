from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def run(*, items: List[int]) -> Optional[TreeNode]:
            if not items:
                return None

            if len(items) == 1:
                return TreeNode(items[0])

            mid = len(items) // 2
            left = run(items=items[:mid])
            right = run(items=items[mid + 1 :])
            return TreeNode(items[mid], left, right)

        return run(items=nums)


solution = Solution()
print(solution.sortedArrayToBST([-10, -3, 0, 5, 9]))
print(solution.sortedArrayToBST([1, 3]))
