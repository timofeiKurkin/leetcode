from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1][:]

        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]

        # for i in range(n - 2, -1, -1):
        #     for j in range(len(triangle[i])):
        #         triangle[i][j] = triangle[i][j] + min(
        #             triangle[i + 1][j], triangle[i + 1][j + 1]
        #         )
        # return triangle[0][0]


solution = Solution()

print(solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
# print(solution.minimumTotal([[-10]]))
# print(solution.minimumTotal([[-1], [2, 3], [1, -1, -3]1]))
