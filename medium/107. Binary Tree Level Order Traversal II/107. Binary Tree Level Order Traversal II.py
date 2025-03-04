from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res: List[List[int]] = []
        queue: deque[TreeNode] = deque([root])

        while len(queue) > 0:
            level_items: List[int] = []
            level_length = len(queue)

            for _ in range(0, level_length):
                curr_node = queue.popleft()

                level_items.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            res.append(level_items)

        res.reverse()
        return res
