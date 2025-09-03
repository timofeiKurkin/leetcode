from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        return self.solution1(points)

    def solution1(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))

        res = 0
        n = len(points)

        for i in range(n):
            top = points[i][1]
            bottom = float("-inf")

            for j in range(i + 1, n):
                y = points[j][1]

                if bottom < y <= top:
                    res += 1
                    bottom = y

                    if bottom == top:
                        break

        return res
