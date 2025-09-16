from math import gcd
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        top = -1

        for x in nums:
            curr = x

            while top != -1:
                g = gcd(nums[top], curr)

                if g == 1:
                    break

                curr = nums[top] // g * curr
                top -= 1

            top += 1
            nums[top] = curr

        return nums[: top + 1]
