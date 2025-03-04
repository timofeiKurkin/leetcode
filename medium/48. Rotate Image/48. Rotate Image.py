from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix[0])):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix[0])):
            matrix[i] = matrix[i][::-1]

        print(matrix)

        # no_right = []
        # for i in range(len(matrix[0])):
        #     items = [item[i] for item in matrix]
        #     no_right.append(items[::-1])
        # matrix = no_right


solution = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution.rotate(matrix=matrix)
