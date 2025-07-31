from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        return self.solution1(nums)

    def solution1(self, nums: List[int]) -> int:
        max_len = [0]
        max_val = 0

        for num in nums:
            if num == max_val:
                max_len[-1] += 1
            elif num > max_val:
                max_val = num
                max_len = [1]
            else:
                max_len.append(0)

        return max(max_len)
