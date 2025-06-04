from functools import cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        return solution3(prices, fee)


def solution1(prices: List[int], fee: int) -> int:
    n = len(prices)

    @cache
    def run(idx: int, taken: int) -> int:
        if idx >= n and taken:
            return 0
        if idx >= n:
            return 0
        if taken:
            return max(run(idx + 1, 1), prices[idx] + run(idx + 1, 0))
        return max(run(idx + 1, 0), (-prices[idx] + run(idx + 1, 1)) - fee)

    return run(0, 0)


def solution2(prices: List[int], fee: int) -> int:
    n = len(prices)

    profit = 0
    hold = [0] * n
    hold[0] = -prices[0]

    for i in range(1, n):
        profit = max(profit, hold[i - 1] + prices[i] - fee)
        hold[i] = max(hold[i - 1], profit - prices[i])

    return profit


def solution3(prices: List[int], fee: int) -> int:
    hold = -prices[0]
    profit = 0

    for p in prices[1:]:
        profit = max(profit, hold + p - fee)
        hold = max(hold, profit - p)

    return profit


solution = Solution()
print(solution.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))  # 8
print(solution.maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))  # 6
