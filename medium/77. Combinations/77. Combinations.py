from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # combinations: List[List[int]] = [[]]

        # for num in range(1, n + 1):
        #     combination = []

        #     for comb in combinations:
        #         if len(comb) < k:
        #             combination.append(comb + [num])

        #     combinations.extend(combination)

        # return [item for item in combinations if len(item) == k]

        result = []

        def backtracking(index: int, path: List[int]) -> None:
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(index, n + 1):
                path.append(i)
                backtracking(i + 1, path)
                path.pop()

        backtracking(1, [])
        return result


solution = Solution()
print(solution.combine(n=4, k=2))
print(solution.combine(n=1, k=1))
