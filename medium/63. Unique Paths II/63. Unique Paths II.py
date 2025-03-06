from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp: List[List[int]] = [[0] * len(obstacleGrid[0]) for _ in range(n)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0

        for i in range(1, n):
            if obstacleGrid[i][0] != 1 and dp[i - 1][0] == 1:
                dp[i][0] = 1

        for j in range(1, m):
            if obstacleGrid[0][j] != 1 and dp[0][j - 1] == 1:
                dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


solution = Solution()
print(
    solution.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]])
)  # 2
print(solution.uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]))  # 1
print(
    solution.uniquePathsWithObstacles(
        obstacleGrid=[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)  # 40
print(solution.uniquePathsWithObstacles(obstacleGrid=[[0]]))  # 1
print(solution.uniquePathsWithObstacles(obstacleGrid=[[1]]))  # 0
print(solution.uniquePathsWithObstacles(obstacleGrid=[[1, 0]]))  # 0
