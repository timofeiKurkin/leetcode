"""
# Definition for a QuadTree node.
"""

from typing import List, Union


class Node:
    def __init__(
        self,
        val: bool,
        isLeaf: bool,
        topLeft: Union["Node", None] = None,
        topRight: Union["Node", None] = None,
        bottomLeft: Union["Node", None] = None,
        bottomRight: Union["Node", None] = None,
    ):
        self.val = val
        self.isLeaf = isLeaf  # if block has only one children, False otherwise
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        def quad_tree(x1: int, x2: int, y1: int, y2: int) -> Node:
            if x1 == x2 and y1 == y2:
                return Node(
                    val=bool(grid[y1][x1]),
                    isLeaf=True,
                )

            x_center, y_center = (x1 + x2) // 2, (y1 + y2) // 2

            topLeft = quad_tree(x1, x_center, y1, y_center)
            topRight = quad_tree(x_center + 1, x2, y1, y_center)
            bottomLeft = quad_tree(x1, x_center, y_center + 1, y2)
            bottomRight = quad_tree(x_center + 1, x2, y_center + 1, y2)

            if (
                topLeft.isLeaf
                and topRight.isLeaf
                and bottomLeft.isLeaf
                and bottomRight.isLeaf
                and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val
            ):
                return Node(val=topLeft.val, isLeaf=True)

            return Node(
                val=True,
                isLeaf=False,
                topLeft=topLeft,
                topRight=topRight,
                bottomLeft=bottomLeft,
                bottomRight=bottomRight,
            )

        return quad_tree(0, len(grid) - 1, 0, len(grid) - 1)


solution = Solution()
print(solution.construct(grid=[[0, 1], [1, 0]]))
print(
    solution.construct(
        grid=[
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
        ]
    )
)
