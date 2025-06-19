from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        res, prev = 0, nums[0]

        for i in range(1, len(nums)):
            if nums[i] - prev > k:
                prev = nums[i]
                res += 1

        return res
