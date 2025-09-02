from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        return self.solution2(points)

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

    def solution2(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (-x[0], x[1]))
        n, res = len(points), 0

        for i in range(n - 1):
            top = 51

            for j in range(i + 1, n):
                if top > points[j][1] >= points[i][1]:
                    res += 1
                    top = points[j][1]

        return res
