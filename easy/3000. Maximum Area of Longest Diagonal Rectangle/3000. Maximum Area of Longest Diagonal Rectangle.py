from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        res = 0

        for length, width in dimensions:
            diagonal = length**2 + width**2

            if diagonal == max_diagonal:
                res = max(res, length * width)
            elif diagonal > max_diagonal:
                max_diagonal = diagonal
                res = length * width

        return res
