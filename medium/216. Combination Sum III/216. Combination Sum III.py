from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n:
            return []

        res = []

        def backtrack(items: List[int], curr_sum: int, combination: List[int]) -> None:
            if curr_sum > n or len(combination) > k:
                return

            if curr_sum == n and len(combination) < k:
                return

            if curr_sum == n:
                res.append(combination)
                return

            for item in items:
                if item not in combination:
                    backtrack(items[1:], curr_sum + item, combination + [item])
                else:
                    return

        backtrack([i for i in range(1, 10)], 0, [])
        return res
