from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        n = len(nums)
        left_sum = 0

        for i in range(n):
            right_sum = total_sum - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1
