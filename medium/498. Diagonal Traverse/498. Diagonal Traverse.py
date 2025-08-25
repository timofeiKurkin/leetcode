from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        return self.solution1(mat)

    def solution1(self, mat: List[List[int]]) -> List[int]:
        n = len(mat[0])
        m = len(mat)

        if m == 1 and n == 1:
            return mat[0]

        def goThroughDiagonal(i: int, j: int) -> List[int]:
            items = []

            while i < m and j >= 0:
                items.append(mat[i][j])
                i += 1
                j -= 1

            return items

        res: List[int] = []
        diagonals = 0

        for j in range(n):
            diagonal = goThroughDiagonal(0, j)

            if diagonals % 2 == 0:
                diagonal.reverse()

            res = res + diagonal
            diagonals += 1

        for i in range(1, m):
            diagonal = goThroughDiagonal(i, n - 1)

            if diagonals % 2 == 0:
                diagonal.reverse()

            res = res + diagonal
            diagonals += 1

        return res

    def solution2(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        i, j = 0, 0
        res: List[int] = []

        for _ in range(m * n):
            res.append(mat[i][j])

            if (i + j) % 2 == 0:
                if j == n - 1:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == m - 1:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    j -= 1
                    i += 1

        return res


print(Solution().findDiagonalOrder(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().findDiagonalOrder(mat=[[1, 2], [3, 4]]))
