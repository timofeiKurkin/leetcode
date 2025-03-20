# from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        state = [0] * numCourses

        def has_cycle(course: int) -> bool:
            if state[course] == 1:
                return True
            if state[course] == 2:
                return False

            state[course] = 1
            for pre in graph[course]:
                if has_cycle(pre):
                    return True

            state[course] = 2
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True


solution = Solution()
# print(solution.canFinish(2, [[1, 0]]))
print(solution.canFinish(2, [[1, 0], [0, 1]]))
print(solution.canFinish(3, [[1, 0], [2, 1]]))
