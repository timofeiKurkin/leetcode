from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.right or not root.left):
            return False

        # queue = deque([root.left, root.right])
        # while queue:
        #     level_len = len(queue)
        #     level_items = []
        #     for _ in range(level_len):
        #         item = queue.popleft()
        #         level_items.append(item.val)
        #         if item.left:
        #             queue.append(item.left)
        #         if item.right:
        #             queue.append(item.right)
        #     if len(level_items) % 2 == 0:
        #         for first, second in zip(
        #             level_items[: len(level_items) // 2],
        #             reversed(level_items[len(level_items) // 2 :]),
        #         ):
        #             if first != second:
        #                 return False
        #     else:
        #         return False
        # return True
        
        # if root.left.val == root.


arr_test = [1, 2, 3, 4]

for first, second in zip(
    arr_test[: len(arr_test) // 2], reversed(arr_test[len(arr_test) // 2 :])
):
    print(first, second)
