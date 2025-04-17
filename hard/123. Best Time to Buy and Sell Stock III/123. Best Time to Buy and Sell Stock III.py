from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy1, buy2 = -prices[0], -prices[0]
        # profit_curr, total_profit = 0, 0

        # for price in prices:
        #     buy1 = max(buy1, -price)
        #     profit_curr = max(profit_curr, buy1 + price)
        #     buy2 = max(buy2, profit_curr - price)
        #     total_profit = max(total_profit, price + buy2)

        # return total_profit

        n = len(prices)
        if not n:
            return n

        max_purchases = 2
        dp = [[0] * n for _ in range(max_purchases + 1)]

        for k in range(1, max_purchases + 1):
            min_price = prices[0]

            for i in range(1, n + 1):
                min_price = min(min_price, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - min_price)

        return dp[max_purchases][-1]


solution = Solution()
print(solution.maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4]))
print(solution.maxProfit(prices=[1, 2, 3, 4, 5]))
print(solution.maxProfit(prices=[7, 6, 4, 3, 1]))
