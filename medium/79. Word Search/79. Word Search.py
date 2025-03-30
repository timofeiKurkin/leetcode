from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        t = len(word)
        m = len(board)
        n = len(board[0])

        def backtrack_dfs(i: int, j: int, index: int) -> bool:
            if index == t:
                return True

            if i < 0 or j < 0 or i == m or j == n or board[i][j] != word[index]:
                return False

            symbol = board[i][j]
            board[i][j] = "#"

            top = backtrack_dfs(i - 1, j, index + 1)
            left = backtrack_dfs(i, j - 1, index + 1)
            bottom = backtrack_dfs(i + 1, j, index + 1)
            right = backtrack_dfs(i, j + 1, index + 1)

            board[i][j] = symbol
            return top or left or bottom or right

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    exist = backtrack_dfs(i, j, 0)
                    if exist:
                        return True

        return False


solution = Solution()

print(
    solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
)
print(
    solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="SEE",
    )
)
print(
    solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
)
print(
    solution.exist(
        board=[
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
        ],
        word="AAAAAAAAAAAABAA",
    )
)
