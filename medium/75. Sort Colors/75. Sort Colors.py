from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()

        count = [0] * (max(nums) + 1)

        for num in nums:
            count[num] += 1

        i = 0
        for num, freq in enumerate(count):
            for _ in range(freq):
                nums[i] = num
                i += 1
