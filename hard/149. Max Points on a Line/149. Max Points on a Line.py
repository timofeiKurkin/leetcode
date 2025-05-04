import math
from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Given an array of points where point = [x, y]
        # Use the line slope formula
        # (y2 - y1) / (x2 - x1)

        # For example: [[1, 4], [2, 3]]:
        # The slope is: (3 - 4) / (2 - 1) = -1 / 1 = -1
        # Next points: [[2, 3], [3, 2]]:
        # The slope is: (2 - 3) / (3 - 2) = -1 / 1 = -1
        # Next points: [[3, 2], [4, 1]]:
        # The slope is: (1 - 2) / (4 - 3) = -1 / 1 = -1
        # So points [[1, 4], [2, 3], [3, 2], [4, 1]] belong to the same line

        # {[slope]: count of points in line with this slope}
        n = len(points)
        res = 0

        for i in range(n):
            hash = defaultdict(int)
            x1, y1 = points[i][0], points[i][1]
            max_count = 0
            same_points = 0

            for j in range(n):
                if points[i] == points[j]:
                    same_points += 1
                    continue

                x2, y2 = points[j][0], points[j][1]
                dx = x2 - x1
                dy = y2 - y1

                if dx == 0:
                    slope = (float("inf"), 0)
                elif dy == 0:
                    slope = (0, float("inf"))
                else:
                    gcd = math.gcd(dx, dy)
                    slope = (dy // gcd, dx // gcd)

                hash[slope] += 1

                if hash[slope] > max_count:
                    max_count = hash[slope]

            line = max_count + same_points
            if line > res:
                res = line

        return res


solution = Solution()
print(solution.maxPoints(points=[[1, 1], [2, 2], [3, 3]]))  # 3
print(solution.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))  # 4
print(
    solution.maxPoints(points=[[0, 0], [94911151, 94911150], [94911152, 94911151]])
)  # 1
print(solution.maxPoints(points=[[2, 3], [3, 3], [-5, 3]]))  # 3

# (1, -1): [
#   [[3, 2], [2, 3]],
#   [[3, 2], [1, 4]],
#   [[4, 1], [2, 3]],
#   [[4, 1], [1, 4]],
#   [[2, 3], [1, 4]]
# ]
