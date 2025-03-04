import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer: List[int] = []

        # for index in range(len(nums)):
        #     k = (index % len(nums)) + 1
        #     filtered = nums[: k - 1] + nums[k:]
        #     answer.append(math.prod(filtered))

        n = len(nums)
        answer: List[int] = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
print(solution.productExceptSelf([0, 0]))
