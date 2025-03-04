from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0, prices[0]]
        profit = 0

        for i, price in enumerate(prices):
            if price < buy[1]:
                buy = [i, price]
            else:
                sell_profit = price - buy[1]
                if sell_profit > profit:
                    profit = sell_profit

        return profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
