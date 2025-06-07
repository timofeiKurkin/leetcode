from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        zeroes, oranges = 0, 0
        queue: Deque[Tuple[int, int]] = deque()

        def valid_position(i: int, j: int) -> bool:
            return i >= 0 and j >= 0 and i < n and j < m and grid[i][j] == 1

        def check_directions(i: int, j: int, queue: Deque[Tuple[int, int]]) -> None:
            if valid_position(i + 1, j):
                queue.append((i + 1, j))
            if valid_position(i, j + 1):
                queue.append((i, j + 1))
            if valid_position(i - 1, j):
                queue.append((i - 1, j))
            if valid_position(i, j - 1):
                queue.append((i, j - 1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    zeroes += 1
                    continue

                if grid[i][j] == 2:
                    oranges += 1
                    check_directions(i, j, queue)

        minutes = 0

        while queue:
            local_oranges = 0

            for _ in range(len(queue)):
                (i, j) = queue.popleft()

                if grid[i][j] != 1:
                    continue

                grid[i][j] = 2
                local_oranges += 1
                check_directions(i, j, queue)

            if local_oranges:
                minutes += 1
                oranges += local_oranges

        if oranges + zeroes != m * n:
            return -1

        return minutes


solution = Solution()

print(solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
