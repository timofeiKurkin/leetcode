from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        if root.right and root.right:
            return

        res: List[float] = []
        queue = deque([root])

        while len(queue) > 0:
            levelSum = 0
            levelSize = len(queue)

            for _ in range(1, levelSize):
                curr_node = queue.popleft()
                levelSum += curr_node.val

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            res.append(levelSum / levelSize)

        return res
