from typing import List


class Solution:
    def __init__(self) -> None:
        self.res = 0
        self.max = 0
        self.nums = []
        self.N = 0

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        for num in nums:
            self.max |= num

        self.nums = nums
        self.N = len(nums)
        self.backtrack(0, 0)
        return self.res

    def backtrack(self, index: int, or_value: int):
        if or_value == self.max:
            self.res += 1

        for i in range(index, self.N):
            self.backtrack(i + 1, or_value | self.nums[i])


print(Solution().countMaxOrSubsets(nums=[3, 1]))
print(Solution().countMaxOrSubsets(nums=[2, 2, 2]))
print(Solution().countMaxOrSubsets(nums=[3, 2, 1, 5]))
