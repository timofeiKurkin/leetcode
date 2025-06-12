from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        maxDiff = 0

        for i in range(2 * n):
            maxDiff = max(maxDiff, nums[i % n] - nums[(i + 1) % n])

        return maxDiff
