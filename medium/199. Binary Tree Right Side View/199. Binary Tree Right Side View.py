from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            right_item = 0
            level_length = len(queue)

            for i in range(level_length):
                curr_node = queue.popleft()

                if i == level_length - 1:
                    right_item = curr_node.val

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            if len(res) and right_item >= res[-1]:
                res.append(right_item)
            else:
                res.append(right_item)

        return res
