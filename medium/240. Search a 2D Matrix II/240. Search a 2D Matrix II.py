from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.solution1(matrix, target)

    def solution1(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) - 1

        while i < len(matrix) and j >= 0:
            curr = matrix[i][j]
            if curr == target:
                return True
            elif curr > target:
                j -= 1
            else:
                i += 1

        return False
