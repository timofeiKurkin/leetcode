from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        remind = k
        count = 0

        n = len(nums)
        res = count
        left = 0

        for right in range(n):
            if nums[right] == 1:
                count += 1
            else:
                if remind:
                    remind -= 1
                    count += 1
                else:
                    while not remind:
                        if nums[left] == 0:
                            remind += 1
                        left += 1
                        count -= 1

                    remind -= 1
                    count += 1

            res = max(res, count)

        return res
