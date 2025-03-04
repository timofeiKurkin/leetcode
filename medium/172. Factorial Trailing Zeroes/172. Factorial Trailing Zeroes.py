# import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        # fact = math.factorial(n)
        # arr = str(fact)[::-1]
        # index = 0
        # for s in arr:
        #     if s != "0":
        #         break
        #     else:
        #         index += 1
        # return index

        zeros = 0
        i = 5

        while i <= n:
            zeros += n // i
            i *= 5

        return zeros


solution = Solution()
print(solution.trailingZeroes(3))
print(solution.trailingZeroes(5))
print(solution.trailingZeroes(0))
print(solution.trailingZeroes(7))
print(solution.trailingZeroes(1574))
