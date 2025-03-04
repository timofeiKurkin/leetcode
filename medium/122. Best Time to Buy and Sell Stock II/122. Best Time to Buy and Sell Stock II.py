# Дано: массив неупорядоченных чисел. Где prices[i] - это цена акции в i день
# Условие: вернуть максимальный профит от покупки-продажи акций. За промежуток всех дней можно покупать-продавать несколько акций, но нельзя одновременно держать несколько купленных акций. Т.е. купил акцию, нашел самый хороший день для продажи и продал. На следующий из дней купил другую акцию и т.д.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(0, len(prices) - 1, 1):
            newProfit = prices[i + 1] - prices[i]
            if newProfit > 0:
                profit += newProfit

        return profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([1, 2, 3, 4, 5]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
