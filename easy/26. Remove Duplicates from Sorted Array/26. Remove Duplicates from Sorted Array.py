from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        unique_index = 0

        for i in range(len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]

        return unique_index + 1
