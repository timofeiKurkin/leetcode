from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth: int = 0
        queue: deque[TreeNode] = deque([root])

        while len(queue) > 0:
            level_size = len(queue)
            depth += 1

            for _ in range(level_size):
                curr_node = queue.popleft()

                if not curr_node.right and not curr_node.left:
                    return depth

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

        return len(queue)
