from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        res: List[List[int]] = []

        for i in range(0, n - 2, 2):
            candidate = nums[i : i + 3]

            if len(candidate) < 3 or abs(candidate[0] - candidate[2]) > k:
                return []

            res.append(candidate)

        return res
