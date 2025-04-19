from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not n:
            return 0

        max_purchases = k
        dp = [[0] * n for _ in range(max_purchases + 1)]

        for purchase in range(1, max_purchases + 1):
            min_price = prices[0]

            for i in range(1, n):
                min_price = min(min_price, prices[i] - dp[purchase - 1][i - 1])
                dp[purchase][i] = max(dp[purchase][i - 1], prices[i] - min_price)

        return dp[k][-1]


solution = Solution()
print(solution.maxProfit(k=2, prices=[2, 4, 1]))
print(solution.maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
