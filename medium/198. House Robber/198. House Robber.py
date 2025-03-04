from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        if len(nums) == 1:
            return nums[0]

        prev_sum1 = 0
        prev_sum2 = nums[0]

        for i in range(1, len(nums)):
            curr = max(prev_sum2, prev_sum1 + nums[i])

            prev_sum1 = prev_sum2
            prev_sum2 = curr

        return prev_sum2


solution = Solution()
print(solution.rob([1, 2, 3, 1]))
print(solution.rob([2, 7, 9, 3, 1]))
print(solution.rob([2, 1, 1, 2]))
