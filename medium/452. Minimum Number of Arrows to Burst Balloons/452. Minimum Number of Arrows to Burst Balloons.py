from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # if len(points) == 1:
        #     return 1
        # points.sort(key=lambda x: x[0])
        # balloons: List[List[int]] = [points[0]]
        # for i in range(1, len(points)):
        #     if points[i][0] <= balloons[-1][1]:
        #         balloons[-1] = [balloons[-1][0], min(balloons[-1][1], points[i][1])]
        #     else:
        #         balloons.append(points[i])
        # return len(balloons)
        
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        
        for i in range(1, len(points)):
            if points[i][0] > end:
                arrows += 1
                end = points[i][1]
        
        return arrows


solution = Solution()
print(solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
