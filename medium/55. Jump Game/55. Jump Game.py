from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        n = len(nums)

        for i, num in enumerate(nums):
            if i > reachable:
                return False

            reachable = max(reachable, i + num)

            if reachable >= n - 1:
                return True

        return False


solution = Solution()
print(solution.canJump([2, 3, 1, 1, 4]))
print(solution.canJump([3, 2, 1, 0, 4]))
print(solution.canJump([1, 0, 3, 1, 0, 0]))
