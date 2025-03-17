from collections import defaultdict
from typing import List, Set


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)
        print(f"{graph=}")

        # Build a graph
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value

        # The DFS function to search the path
        def dfs(start: str, end: str, visited: Set):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return result * weight

            return -1.0

        print(f"{graph=}")

        # Handle queries
        results = []
        for C, D in queries:
            results.append(dfs(C, D, set()))

        return results


solution = Solution()
print(
    solution.calcEquation(
        equations=[["a", "b"], ["b", "c"]],
        values=[2.0, 3.0],
        queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    )
)
