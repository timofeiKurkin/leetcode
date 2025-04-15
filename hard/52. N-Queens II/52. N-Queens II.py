class Solution:
    def totalNQueens(self, n: int) -> int:
        # Clues:
        # 1. cols set with queens
        # 2. positive and negative diagonals with queens
        # The rule for positive diagonal: row + column
        # The rule for negative diagonal: row - column

        col = set()
        posDiag = set()
        negDiag = set()

        self.res = 0

        def backtrack(r: int) -> None:
            if r == n:
                self.res += 1
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return self.res
