from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict = {}

        for i, val in enumerate(nums):
            difference = target - val
            if difference in seen:
                return [seen[difference], i]

            seen[val] = i

        return []


solution = Solution()
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))
print(solution.twoSum([2, 7, 11, 15], 9))
