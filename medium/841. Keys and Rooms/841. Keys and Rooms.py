from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        # Does not work
        # graph = defaultdict(bool)
        # graph[0] = True

        # def dfs(target: int) -> bool:
        #     for i in range(target + 1, n):
        #         room = rooms[i]
        #         if room and target in room and graph[i]:
        #             for key in room:
        #                 graph[key] = True
        #             return True
        #     return False
        # for i, room in enumerate(rooms):
        #     if not graph[i]:
        #         if not dfs(i):
        #             return False
        #     for key in room:
        #         graph[key] = True
        # return True

        visited = set()

        def dfs(idx: int) -> None:
            if idx in visited:
                return
            visited.add(idx)
            for room in rooms[idx]:
                dfs(room)

        dfs(0)
        return n == len(visited)


solution = Solution()
print(solution.canVisitAllRooms([[1], [2], [3], []]))
print(solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
print(solution.canVisitAllRooms([[2], [], [1]]))
print(solution.canVisitAllRooms([[1, 3], [1, 4], [2, 3, 4, 1], [], [4, 3, 2]]))
