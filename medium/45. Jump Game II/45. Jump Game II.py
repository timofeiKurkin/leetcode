from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        reachable = 0
        current_end = 0
        steps = 0

        for i, num in enumerate(nums[:-1]):
            reachable = max(reachable, num + i)

            if current_end == i:
                current_end = reachable
                steps += 1

            if current_end >= len(nums) - 1:
                break

        return steps


solution = Solution()
print(solution.jump([2, 3, 1, 1, 4]))
print(solution.jump([2, 3, 0, 1, 4]))
print(solution.jump([1]))
print(solution.jump([1, 2, 1, 1, 1]))
print(solution.jump([2, 1]))
