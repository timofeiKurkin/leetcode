from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        return self.solution2(grid)

    def solution1(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        def goThroughDiagonal(i: int, j: int, reverse: bool = False):
            items = []

            while i < n and j < n:
                items.append(grid[i][j])
                i += 1
                j += 1

            items.sort(reverse=reverse)
            i -= 1
            j -= 1

            while i >= 0 and j >= 0:
                grid[i][j] = items.pop()
                i -= 1
                j -= 1

        for i in range(n):
            goThroughDiagonal(i, 0, True)

        for j in range(1, n):
            goThroughDiagonal(0, j)

        return grid

    def solution2(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for d in range(1, n):
            items = sorted(grid[i][i + d] for i in range(n - d))
            for i, v in enumerate(items):
                grid[i][i + d] = v

        for d in range(n):
            items = sorted((grid[j + d][j] for j in range(n - d)), reverse=True)
            for j, v in enumerate(items):
                grid[d + j][j] = v

        return grid
