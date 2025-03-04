from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                i = max(i - 1, 0)
            else:
                i += 1

        return len(nums)


solution = Solution()
print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
