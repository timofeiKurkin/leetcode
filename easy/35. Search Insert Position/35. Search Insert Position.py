from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def run(index: int) -> int:
            if not nums or index >= len(nums):
                return index

            if nums and (nums[index] >= target or target == nums[index]):
                return index

            return run(index + 1)

        return run(0)


solution = Solution()
print(solution.searchInsert(nums=[1, 3, 5, 6], target=5))
print(solution.searchInsert(nums=[1, 3, 5, 6], target=2))
print(solution.searchInsert(nums=[1, 3, 5, 6], target=7))
