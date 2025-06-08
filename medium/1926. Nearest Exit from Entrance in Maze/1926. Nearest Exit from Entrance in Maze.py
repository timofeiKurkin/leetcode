from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # TLE
        # n = len(maze)
        # m = len(maze[0])
        # inf = 10**10

        # def dfs(i: int, j: int, curr_steps: int) -> int:
        #     if i < 0 or j < 0 or i >= n or j >= m or maze[i][j] == "+":
        #         return inf
        #     if i == 0 or i == n - 1 or j == 0 or j == m - 1:
        #         return curr_steps
        #     maze[i][j] = "+"
        #     top = dfs(i - 1, j, curr_steps + 1)
        #     right = dfs(i, j + 1, curr_steps + 1)
        #     bottom = dfs(i + 1, j, curr_steps + 1)
        #     left = dfs(i, j - 1, curr_steps + 1)
        #     maze[i][j] = "."
        #     return min(top, right, left, bottom)

        # steps = inf

        # for num in range(4):
        #     i, j = entrance
        #     # 0 - top;
        #     if num == 0:
        #         steps = min(steps, dfs(i - 1, j, 1))
        #     # 1 - right;
        #     if num == 1:
        #         steps = min(steps, dfs(i, j + 1, 1))
        #     # 2 - bottom;
        #     if num == 2:
        #         steps = min(steps, dfs(i + 1, j, 1))
        #     # 3 - left;
        #     if num == 3:
        #         steps = min(steps, dfs(i, j - 1, 1))

        # return steps if steps != inf else -1

        n, m = len(maze), len(maze[0])
        queue: Deque[Tuple[int, int, int]] = deque()
        queue.append((entrance[0], entrance[1], 0))
        visited = set()
        visited.add((entrance[0], entrance[1]))

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while queue:
            row, col, steps = queue.popleft()

            if (row == 0 or row == n - 1 or col == 0 or col == m - 1) and (
                row != entrance[0] or col != entrance[1]
            ):
                return steps

            for d_row, d_col in directions:
                new_row, new_column = row + d_row, col + d_col

                if (
                    0 <= new_row < n
                    and 0 <= new_column < m
                    and maze[new_row][new_column] == "."
                    and (new_row, new_column) not in visited
                ):
                    visited.add((new_row, new_column))
                    queue.append((new_row, new_column, steps + 1))

        return -1


solution = Solution()
print(
    solution.nearestExit(
        maze=[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
        entrance=[1, 2],
    )
)
print(
    solution.nearestExit(
        maze=[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], entrance=[1, 0]
    )
)
print(
    solution.nearestExit(
        [
            [".", ".", ".", ".", ".", "+", ".", ".", "."],
            [".", "+", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "+", ".", "+", ".", "+", ".", "+"],
            [".", ".", ".", ".", "+", ".", ".", ".", "."],
            [".", ".", ".", ".", "+", "+", ".", ".", "."],
            ["+", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "+", ".", ".", ".", ".", "."],
            [".", ".", ".", "+", ".", ".", ".", ".", "+"],
            ["+", ".", ".", "+", ".", "+", "+", ".", "."],
        ],
        [8, 4],
    )
)
