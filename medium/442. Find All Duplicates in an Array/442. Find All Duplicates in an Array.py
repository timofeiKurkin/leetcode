from typing import List, Set


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return self.solution2(nums)

    def solution1(self, nums: List[int]) -> List[int]:
        items: Set[int] = set()
        res = []

        for num in nums:
            if num in items:
                res.append(num)
            else:
                items.add(num)

        return res

    def solution2(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                res.append(index + 1)
            else:
                nums[index] = -nums[index]

        return res
