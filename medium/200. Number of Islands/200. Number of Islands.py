from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def dfs(i: int, j: int) -> None:
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)

        return islands


solution = Solution()
print(
    solution.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)  # 1
print(
    solution.numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)  # 3
print(solution.numIslands([["1", "1", "1"], ["0", "1", "0"], ["0", "1", "0"]]))  # 1
print(solution.numIslands([["1"], ["0"], ["1"], ["0"], ["1"], ["1"]]))  # 3
print(solution.numIslands([["1", "0", "1", "1", "0", "1", "1"]]))  # 3
print(
    solution.numIslands(
        [
            ["1", "1", "0", "1", "1"],
            ["1", "1", "0", "0", "1"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)  # 3
