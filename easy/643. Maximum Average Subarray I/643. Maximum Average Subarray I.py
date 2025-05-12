from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        res = float("-inf")
        curr_sum = sum(nums[: k - 1])
        left = 0

        for right in range(k - 1, n):
            curr_sum += nums[right]
            res = max(res, curr_sum / k)
            curr_sum -= nums[left]
            left += 1

        return res
