from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return amount

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float("inf") else -1


solution = Solution()
print(solution.coinChange(coins=[1, 2, 5], amount=11))
