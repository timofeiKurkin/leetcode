from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []
        n = len(candidates)
        candidates.sort()

        def backtrack(nums: List[int], remaining: int, i: int) -> None:
            if remaining == 0:
                res.append(nums[:])
                return

            for j in range(i, n):
                curr = candidates[j]
                if j > i and curr == candidates[j - 1]:
                    continue

                if curr > remaining:
                    break

                nums.append(curr)
                backtrack(nums, remaining - curr, j + 1)
                nums.pop()

        backtrack([], target, 0)

        return res


solution = Solution()
print(solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
print(solution.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
print(solution.combinationSum2(candidates=[1, 1], target=2))
print(
    solution.combinationSum2(
        candidates=[
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            33,
            3,
            3,
            3,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            44,
            4,
            4,
            4,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            49,
            5,
            5,
            5,
            5,
            6,
            6,
            6,
            6,
        ],
        target=29,
    )
)


# print([1, 1][1:])
