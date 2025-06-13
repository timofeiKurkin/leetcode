from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []

        def backtrack(path: List[int], arr: List[int]):
            res.append(path)

            if not arr:
                return

            for i in range(len(arr)):
                backtrack(path + [arr[i]], arr[i + 1 :])

        backtrack([], nums)

        return res


solution = Solution()
print(solution.subsets(nums=[1, 2, 3]))
