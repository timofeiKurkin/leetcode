from collections import deque
from typing import Deque

"""
# Definition for a Node.
"""


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        queue: Deque[Node | None] = deque([root])

        while queue:
            prev: Node | None = None

            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    if not prev:
                        prev = node
                    else:
                        prev.next = node
                        prev = node

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            if prev:
                prev.next = None

        return root
