from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # m = len(board)
        # n = len(board[0])

        # def getCell(i: int, j: int) -> int | None:
        #     if i < 0 or j < 0 or i >= m or j >= n:
        #         return None

        #     return board[i][j]

        # def checkRules(i: int, j: int) -> None:
        #     curr_cell = board[i][j]
        #     top, bottom, right, left = i - 1, i + 1, j + 1, j - 1

        #     one = 0

        #     top_cell = getCell(top, j)
        #     left_cell = getCell(i, left)
        #     right_cell = getCell(i, right)
        #     bottom_cell = getCell(bottom, j)
        #     top_right_cell = getCell(top, right)
        #     top_left_cell = getCell(top, left)
        #     bottom_left_cell = getCell(bottom, left)
        #     bottom_right_cell = getCell(bottom, right)

        #     for num in [
        #         top_cell,
        #         left_cell,
        #         right_cell,
        #         bottom_cell,
        #         top_right_cell,
        #         top_left_cell,
        #         bottom_left_cell,
        #         bottom_right_cell,
        #     ]:
        #         if num is not None and (num == 1 or num == -1):
        #             one += 1

        #     if curr_cell == 1:
        #         if one < 2 or one > 3:
        #             board[i][j] = -1

        #     else:
        #         if one == 3:
        #             board[i][j] = -2

        # for i in range(m):
        #     for j in range(n):
        #         checkRules(i, j)

        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == -1:
        #             board[i][j] = 0
        #         elif board[i][j] == -2:
        #             board[i][j] = 1

        m, n = len(board), len(board[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]

        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                        live_neighbors += 1

                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
