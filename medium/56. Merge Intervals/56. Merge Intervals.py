from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda val: val[0])  # [[1, 3], [2, 6], [8, 10], [15, 18]]

        res: List[List[int]] = [intervals[0]]  # [[1, 3]]

        for i in range(1, len(intervals)):  # go through each element
            if intervals[i][0] <= res[-1][1]:  # if 2 <= 3
                res[-1] = [
                    res[-1][0],
                    max(res[-1][1], intervals[i][1]),
                ]  # [1, max(3, 6)]
            else:
                res.append(intervals[i])

        return res


solution = Solution()

print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# print(solution.merge([[1, 4], [4, 5]]))
