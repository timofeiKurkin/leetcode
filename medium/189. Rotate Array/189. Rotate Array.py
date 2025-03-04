# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # if not k:
        #     return

        # i = 0
        # k = k // len(nums) if k - 1 > len(nums) else k

        # while i < len(nums):
        #     if len(nums) % 2 == 0:
        #         if i >= k:
        #             item = nums.pop()
        #             nums.insert(0, item)
        #     else:
        #         if i > k:
        #             item = nums.pop()
        #             nums.insert(0, item)
        #     i += 1

        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
        print(f"{nums=}")


solution = Solution()

case_1 = [1, 2, 3, 4, 5, 6, 7]
case_2 = [-1, -100, 3, 99]
case_3 = [1, 2]
case_4 = [1, 2, 3]

solution.rotate(case_1, 3)
solution.rotate(case_2, 2)
solution.rotate(case_3, 3)
solution.rotate(case_4, 2)
