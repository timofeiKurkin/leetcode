from typing import List


class Solution:
    def unique_items(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                res.append(nums[i])

        res.append(nums[-1])

        return res

    def countHillValley(self, nums: List[int]) -> int:
        return self.solution1(nums)

    def solution1(self, nums: List[int]) -> int:
        unique_nums = self.unique_items(nums)
        res = 0
        n = len(unique_nums)

        for i in range(1, n - 1):
            if unique_nums[i - 1] < unique_nums[i] > unique_nums[i + 1]:
                res += 1
            elif unique_nums[i - 1] > unique_nums[i] < unique_nums[i + 1]:
                res += 1

        return res
