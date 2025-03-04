from itertools import chain
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(row: List[int]) -> bool:
            unique = set({})
            for item in row:
                if item != ".":
                    if item in unique:
                        return False
                    unique.add(item)
            return True

        for x, y in zip(range(9), range(9)):
            row_is_valid = is_valid(board[x])
            column_is_valid = is_valid([item[y] for item in board])

            if not row_is_valid or not column_is_valid:
                return False

        i = 1
        x, y = 0, 0
        while x != 9 and y != 9:
            square_valid = is_valid(
                list(chain(*[item[y : y + 3] for item in board][x : x + 3]))
            )

            if not square_valid:
                return False

            y += 3
            i += 1

            if y == 9 and i != 9:
                y = 0
                x += 3

        return True

        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]
        # blocks = [set() for _ in range(9)]

        # for r in range(9):
        #     for c in range(9):
        #         num = board[r][c]
        #         if num == ".":
        #             continue

        #         block_index = (r // 3) * 3 + (c // 3)

        #         if num in rows[r] or num in cols[c] or num in blocks[block_index]:
        #             return False

        #         rows[r].add(num)
        #         cols[c].add(num)
        #         blocks[block_index].add(num)

        # return True


solution = Solution()

sudoku_1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

sudoku_2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

sudoku_3 = [
    ["4", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(solution.isValidSudoku(sudoku_1))
print(solution.isValidSudoku(sudoku_2))
print(solution.isValidSudoku(sudoku_3))
