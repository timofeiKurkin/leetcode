from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return self.solution2(nums)

    def solution1(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        @cache
        def run(i: int, curr_sum: int) -> bool:
            if i >= len(nums):
                return False
            if curr_sum == total_sum // 2:
                return True
            return run(i + 1, curr_sum) or run(i + 1, curr_sum + nums[i])

        return run(0, 0)

    def solution2(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]


solution = Solution()
print(solution.canPartition(nums=[1, 5, 11, 5]))
# nums = [1, 2, 3, 4, 5]
