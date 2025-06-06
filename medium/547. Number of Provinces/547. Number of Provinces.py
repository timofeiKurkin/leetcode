from typing import List


class Solution:
    def findCircleNum(self, connections: List[List[int]]) -> int:
        n = len(connections)
        res = 0

        visited = set()

        def dfs(city: int):
            if city > n or city in visited:
                return

            visited.add(city)
            for i, conn in enumerate(connections[city]):
                if conn:
                    dfs(i)

        for city in range(n):
            if city in visited:
                continue
            dfs(city)
            res += 1

        return res
