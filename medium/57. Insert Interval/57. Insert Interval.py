from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # if not intervals:
        #     return [newInterval]

        # intervals.sort(key=lambda val: val[0])

        # res: List[List[int]] = []

        # if newInterval[1] < intervals[0][0]:
        #     res = [newInterval, *intervals]
        # elif newInterval[0] > intervals[-1][1]:
        #     res = [*intervals, newInterval]
        # else:
        #     for i in range(len(intervals)):
        #         if (
        #             newInterval[0] <= intervals[i][1]
        #             and newInterval[1] >= intervals[i][0]
        #         ):
        #             if not res or (
        #                 res[-1][1] < newInterval[0] and res[-1][0] < newInterval[1]
        #             ):
        #                 res.append(
        #                     [
        #                         min(intervals[i][0], newInterval[0]),
        #                         max(intervals[i][1], newInterval[1]),
        #                     ]
        #                 )
        #             else:
        #                 res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
        #         elif (
        #             res
        #             and newInterval[0] > res[-1][1]
        #             and newInterval[1] < intervals[i][0]
        #         ):
        #             res.append(newInterval)
        #             res.append(intervals[i])
        #         else:
        #             res.append(intervals[i])

        # return res

        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res


solution = Solution()

print(solution.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
print(
    solution.insert(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
    )
)
