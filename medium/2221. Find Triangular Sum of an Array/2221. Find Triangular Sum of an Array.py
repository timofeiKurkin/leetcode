from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        return self.solution1(nums)

    def solution1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n - i) for i in range(n)]
        dp[0] = nums

        for i in range(1, n):
            for j in range(n - i):
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1]) % 10

        return dp[-1][0]

    def solution2(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 0:
            for i in range(n - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            n -= 1

        return nums[0]
