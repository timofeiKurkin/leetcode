from functools import cache


class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def run(n: int) -> int:
            if n == 0:
                return 0
            if n <= 2:
                return 1
            return run(n - 1) + run(n - 2) + run(n - 3)

        return run(n)
