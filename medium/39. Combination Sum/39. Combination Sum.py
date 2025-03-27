from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []
        n = len(candidates)

        def backtrack(items: List[int], curr_sum: int, i: int) -> None:
            if i >= n or curr_sum > target:
                return
            if curr_sum == target:
                res.append(items)
                return

            another_item = candidates[i]
            comb_copy = items.copy()
            comb_copy.append(another_item)

            backtrack(comb_copy, curr_sum + another_item, i)

            backtrack(items, curr_sum, i + 1)

            return

        backtrack([], 0, 0)

        return res


solution = Solution()
print(solution.combinationSum(candidates=[2, 3, 6, 7], target=7))
print(solution.combinationSum(candidates=[2, 3, 5], target=8))
print(solution.combinationSum(candidates=[2], target=1))
