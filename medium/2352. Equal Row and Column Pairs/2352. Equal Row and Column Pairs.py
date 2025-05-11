from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # ver: defaultdict[tuple, int] = defaultdict(int)
        # hor: defaultdict[tuple, int] = defaultdict(int)

        # n = len(grid)

        # for r in range(n):
        #     hor[tuple(grid[r])] += 1
        #     rev = tuple(reversed(grid[r]))
        #     hor[rev] += 1

        # for c in range(n):
        #     key = []
        #     for r in range(n):
        #         key.append(grid[r][c])

        #     ver[tuple(key)] += 1
        #     rev = tuple(reversed(key))
        #     ver[rev] += 1

        # res = 0

        # for key in ver:
        #     while ver[key]:
        #         if key in hor and hor[key]:
        #             res += 1
        #             hor[key] -= 1

        #         ver[key] -= 1

        # return res

        row = defaultdict(int)
        n = len(grid)

        for r in range(n):
            row[tuple(grid[r])] += 1

        res = 0

        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            res += row[col]

        return res


solution = Solution()
print(solution.equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
