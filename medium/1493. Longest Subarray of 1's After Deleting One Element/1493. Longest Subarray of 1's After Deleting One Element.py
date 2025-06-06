from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        # left = 0
        # res = nums[0]
        # remind = 1 if res else 0

        # for right in range(1, len(nums)):
        #     if nums[right] == 1:
        #         res = max(res, right - left)

        #     if nums[right] == 0:
        #         if remind:
        #             remind = 0
        #         else:
        #             while not remind:
        #                 if nums[left] == 0:
        #                     remind = 1
        #                 left += 1
        #             remind = 0

        # return res

        left = 0
        res = 0
        zeroes = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1

            while zeroes > 1:
                zeroes -= 1 if not nums[left] else 0
                left += 1

            res = max(res, right - left)

        return res
