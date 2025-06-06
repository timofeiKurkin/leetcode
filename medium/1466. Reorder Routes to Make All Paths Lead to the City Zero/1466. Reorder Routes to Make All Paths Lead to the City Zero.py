from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        res = 0

        while len(visited) < n:
            check = []

            for conn in connections:
                if conn[1] in visited:
                    visited.add(conn[0])
                elif conn[0] in visited:
                    visited.add(conn[1])
                    res += 1
                else:
                    check.append(conn)

            connections = check[::-1]

        return res
