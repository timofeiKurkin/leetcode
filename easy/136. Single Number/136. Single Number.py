from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = 0

        for num in nums:
            res = res ^ num

        return res


solution = Solution()
print(solution.singleNumber([4, 1, 2, 1, 2]))
