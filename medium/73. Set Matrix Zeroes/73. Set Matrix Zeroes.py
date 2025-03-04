from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # m = len(matrix)
        # n = len(matrix[0])
        # def dfs(i: int, j: int, way: int = -1) -> None:
        #     if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] == 0:
        #         return
        #     matrix[i][j] = "T"
        #     if way == 1:
        #         dfs(i + 1, j, way)
        #     elif way == 2:
        #         dfs(i - 1, j, way)
        #     elif way == 3:
        #         dfs(i, j + 1, way)
        #     elif way == 4:
        #         dfs(i, j - 1, way)
        #     else:
        #         dfs(i + 1, j, 1)
        #         dfs(i - 1, j, 2)
        #         dfs(i, j + 1, 3)
        #         dfs(i, j - 1, 4)
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             matrix[i][j] = "T"
        #             dfs(i, j)
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == "T":
        #             matrix[i][j] = 0

        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        columns = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows or j in columns:
                    matrix[i][j] = 0


solution = Solution()

matrix_1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(matrix_1)
print(matrix_1)

matrix_2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solution.setZeroes(matrix_2)
print(matrix_2)
