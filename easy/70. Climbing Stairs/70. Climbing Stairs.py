from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 0 or n == 1:
        #     return 1

        # a, b = 1, 1

        # for i in range(2, n + 1, 1):
        #     curr = b + a
        #     b = a
        #     a = curr

        # return a

        @cache
        def run(ways: int) -> int:
            if ways > n:
                return 0
            if ways == n:
                return 1
            return run(ways + 1) + run(ways + 2)

        return run(0)
