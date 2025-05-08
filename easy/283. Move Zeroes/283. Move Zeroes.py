from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums = nums[:i] + nums[i + 1 :]  # + [-1]
                # nums.append(nums[i])


solution = Solution()

case_1 = [0, 1, 0, 3, 12]
solution.moveZeroes(case_1)
print(case_1)
