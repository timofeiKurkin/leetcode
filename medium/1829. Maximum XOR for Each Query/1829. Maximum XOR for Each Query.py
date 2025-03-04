from collections import deque
from functools import reduce
from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # new_n: deque[int] = deque(nums)
        # items: List[int] = []

        # for i in range(len(nums)):
        #     xor_sum = reduce(lambda x, y: x ^ y, nums)
        #     k = (2**maximumBit) - 1
        #     items.append(k - xor_sum)
        #     if i:
        #         nums.pop(-1)

        # return items

        k = (1 << maximumBit) - 1
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        items: List[int] = []
        for item in reversed(nums):
            items.append(k ^ xor_sum)
            xor_sum ^= item

        return items


solution = Solution()
print(solution.getMaximumXor([0, 1, 1, 3], 2))
print(solution.getMaximumXor([2, 3, 4, 7], 3))
print(solution.getMaximumXor([0, 1, 2, 2, 5, 7], 3))
