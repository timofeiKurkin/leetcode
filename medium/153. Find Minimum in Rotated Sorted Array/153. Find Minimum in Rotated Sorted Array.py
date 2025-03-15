from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        middle = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                middle = i + 1
                break

        return nums[middle]
