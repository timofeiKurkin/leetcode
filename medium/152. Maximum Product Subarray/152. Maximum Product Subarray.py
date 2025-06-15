from functools import cache
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.solution2(nums)

    def solution1(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def run(index: int, total: int) -> int:
            if index == n:
                return total
            if not total:
                return max(total, run(index + 1, nums[index]))
            if not nums[index]:
                return max(total, run(index + 1, 0))
            return max(
                total,
                run(index + 1, total * nums[index]),
                run(index + 1, nums[index]),
            )

        return run(0, 0)

    def solution2(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = dp_min[0] = nums[0]
        res = nums[0]

        for i in range(1, n):
            num = nums[i]
            dp_max[i] = max(num, dp_max[i - 1] * num, dp_min[i - 1] * num)
            dp_min[i] = min(num, dp_max[i - 1] * num, dp_min[i - 1] * num)
            res = max(res, dp_max[i])

        return res


solution = Solution()

print(solution.maxProduct(nums=[2, 3, -2, 4]))  # 6
print(solution.maxProduct(nums=[-2, 0, -1]))  # 0
print(solution.maxProduct(nums=[3, -7, 1, -9, 2]))  # 378
print(solution.maxProduct(nums=[0, 2]))  # 2
print(solution.maxProduct(nums=[3, 1, -5, 2, 1, -10, 0, 2, 3, 5]))  # 300
print(solution.maxProduct(nums=[3, -1, 4]))  # 4
