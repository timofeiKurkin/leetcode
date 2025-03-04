from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        def dfs(
            i: int,
            j: int,
        ):
            if i == m or j == n or i < 0 or j < 0 or board[i][j] == "X":
                return

            if board[i][j] == "T":
                return

            board[i][j] = "T"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(m):  # y
            for j in range(n):  # x
                if board[i][j] == "O" and (
                    i == 0 or i == m - 1 or j == 0 or j == n - 1
                ):
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


solution = Solution()

board_1 = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
solution.solve(board=board_1)
print(board_1)

board_2 = [["X"]]
solution.solve(board=board_2)
print(board_2)

board_3 = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
solution.solve(board_3)
print(board_3)
