from collections import deque
from typing import Deque, List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # graph tree
        # collect visited squares
        n = len(board)
        board.reverse()

        def getIntoPosition(square: int) -> List[int]:
            row = (square - 1) // n
            column = (square - 1) % n
            if row % 2:
                column = n - 1 - column
            return [row, column]

        q: Deque[List[int]] = deque([[1, 0]])
        visited = set()

        while q:
            square, steps = q.popleft()

            # A cycle in standard 6-sided die roll
            for i in range(1, 7):
                next_square = square + i
                row, column = getIntoPosition(next_square)
                if board[row][column] != -1:
                    next_square = board[row][column]
                if next_square == n**2:
                    return steps + 1
                if next_square not in visited:
                    visited.add(next_square)
                    q.append([next_square, steps + 1])

        return -1


solution = Solution()
print(
    solution.snakesAndLadders(
        board=[
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ]
    )
)
print(solution.snakesAndLadders(board=[[-1, -1], [-1, 3]]))
