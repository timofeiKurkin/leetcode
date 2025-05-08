from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        end = len(nums) - 1
        start = 0
        res = 0

        while start < end:
            if nums[start] == k:
                start += 1
                continue
            if nums[end] == k:
                end -= 1
                continue

            if nums[start] + nums[end] == k:
                res += 1
                start += 1
                end -= 1
            else:
                if k - nums[end] >= nums[start]:
                    start += 1
                else:
                    end -= 1

        return res
