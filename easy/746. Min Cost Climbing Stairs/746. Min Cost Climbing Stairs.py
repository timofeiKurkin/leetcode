from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # # MLE
        # @cache
        # def run(idx: int, total: int) -> int:
        #     if idx >= n:
        #         return total
        #     return min(run(idx + 1, total + cost[idx]), run(idx + 1, total + cost[idx]))

        # return min(run(0, 0), run(1, 0))

        dp = [0] * n
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]

        for i in range(n - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[:2])


solution = Solution()
print(solution.minCostClimbingStairs(cost=[10, 15, 20]))
print(solution.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
