from typing import List, Tuple


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        state = [0] * numCourses
        course_order = set()

        def has_cycle(course: int) -> Tuple[bool, int]:
            if not graph[course]:
                return True, state[course]
            if course in course_order:
                return False, float("Infinity")

            course_order.add(course)
            for pre in graph[course]:
                doable, order = has_cycle(pre)
                if not doable:
                    return False, float("Infinity")
                state[course] = max(state[course], 1 + order)

            graph[course] = []

            return True, state[course]

        for course in range(numCourses):
            doable, _ = has_cycle(course)
            if not doable:
                return []

        return sorted(list(range(numCourses)), key=lambda i: state[i])


solution = Solution()
print(solution.findOrder(numCourses=2, prerequisites=[[1, 0]]))
print(solution.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
print(solution.findOrder(numCourses=4, prerequisites=[[0, 1], [0, 2], [3, 1], [3, 2]]))
print(solution.findOrder(numCourses=1, prerequisites=[]))
