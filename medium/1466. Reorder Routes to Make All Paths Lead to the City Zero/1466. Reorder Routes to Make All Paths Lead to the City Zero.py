from typing import List


class Solution:
    def dfs(self, al: List[List[int]], visited: List[bool], from_city: int) -> int:
        change = 0
        visited[from_city] = True
        for to_city in al[from_city]:
            if not visited[abs(to_city)]:
                change += self.dfs(al, visited, abs(to_city)) + (
                    1 if to_city > 0 else 0
                )
        return change

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # visited = set()
        # res = 0
        # while len(visited) < n:
        #     check = []
        #     for conn in connections:
        #         if conn[1] in visited:
        #             visited.add(conn[0])
        #         elif conn[0] in visited:
        #             visited.add(conn[1])
        #             res += 1
        #         else:
        #             check.append(conn)
        #     connections = check[::-1]
        # return res

        al = [[] for _ in range(n)]
        for c in connections:
            al[c[0]].append(c[1])
            al[c[1]].append(-c[0])
        visited = [False] * n

        return self.dfs(al, visited, 0)
