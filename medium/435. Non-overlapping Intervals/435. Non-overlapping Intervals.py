from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        print(f"{intervals=}")

        deleted = 0
        prev = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev:
                deleted += 1
            else:
                prev = intervals[i][1]

        return deleted


solution = Solution()
print(solution.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))
print(solution.eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]))
print(solution.eraseOverlapIntervals(intervals=[[1, 2], [2, 3]]))
print(solution.eraseOverlapIntervals(intervals=[[1, 100], [11, 22], [1, 11], [2, 12]]))
