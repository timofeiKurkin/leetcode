from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)

        if n == 1:
            return 0

        hash = defaultdict(int)

        for i in range(n):
            domino = (dominoes[i][0], dominoes[i][1])

            if domino in hash:
                hash[domino] += 1
            elif domino[::-1] in hash:
                hash[domino[::-1]] += 1
            else:
                hash[domino] += 1

        res = 0

        for v in hash.values():
            res += v * (v - 1) // 2

        return res


solution = Solution()
print(solution.numEquivDominoPairs(dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]]))
print(solution.numEquivDominoPairs(dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))
