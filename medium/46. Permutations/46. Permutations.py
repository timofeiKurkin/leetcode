from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # if len(nums) == 1:
        #     return [nums]
        # return [list(item) for item in list(permutations(nums, len(nums)))]

        def backtrack(path, arr):
            if not arr:
                res.append(path)
                return
            for i in range(len(arr)):
                backtrack(path + [arr[i]], arr[:i] + arr[i + 1 :])

        res: List[List[int]] = []
        backtrack([], nums)
        return res


solution = Solution()
print(solution.permute([1, 2, 3]))
print(solution.permute([0, 1]))
print(solution.permute([1]))
