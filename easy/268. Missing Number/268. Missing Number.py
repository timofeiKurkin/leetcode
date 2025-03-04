from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort(key=lambda num: num)
        for index in range(0, len(nums)):
            if index != nums[index]:
                return index
        return len(nums)


solution = Solution()
