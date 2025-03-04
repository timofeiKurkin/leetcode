# Дано: массив целочисленных чисел. Побитовое И - операция, при которой определяется сколько битов в остатке между двумя числами.
# Условие: найти самую длинную комбинацию, при которой побитовое И будет самым большим.

from functools import reduce
from typing import Dict, List

case_1 = [16, 17, 71, 62, 12, 24, 14]  # 4
case_2 = [8, 8]  # 2
case_3 = [2, 8]  # 1
case_4 = [2, 6]  # 2
case_5 = [2, 6, 3, 12, 83]  # 4
case_6 = [
    13,
    44,
    58,
    17,
    23,
    13,
    87,
    79,
    91,
    47,
    86,
    90,
    4,
    93,
    18,
    75,
    29,
    66,
    43,
    60,
    19,
    3,
    28,
]  # 14


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        if len(candidates) == 1:
            return 1

        # combination: List[int] = []
        # for i in range(len(candidates)):
        #     bitwise = reduce(lambda x, y: x & y, combination + [candidates[i]])
        #     if bitwise:
        #         combination.append(candidates[i])
        # return len(combination)

        combinations: Dict[int, List[int]] = {}

        for i in range(len(candidates)):
            for j in range(len(candidates)):
                if candidates[j] != candidates[i]:
                    bitwise = candidates[i] & candidates[j]
                    if bitwise:
                        if bitwise not in combinations:
                            combinations[bitwise] = [candidates[i], candidates[j]]
                        elif candidates[j] not in combinations[bitwise]:
                            combinations[bitwise].append(candidates[j])

        best: List[int] = []

        for key in combinations:
            if len(combinations[key]) > len(best):
                best = combinations[key]

        return len(best)

        # best = 0

        # for i in range(24):
        #     count = 0

        #     for num in candidates:
        #         count += (num >> i) & 1

        #     best = max(best, count)

        # return best


solution = Solution()

print(solution.largestCombination(case_1))
print(solution.largestCombination(case_2))
print(solution.largestCombination(case_3))
print(solution.largestCombination(case_4))
print(solution.largestCombination(case_5))
print(solution.largestCombination(case_6))


# print(12 & 17)
# print(12 & 71)
# print(12 & 62)
# print(12 & 16)
# print(12 & 24)
# print(12 & 14)
