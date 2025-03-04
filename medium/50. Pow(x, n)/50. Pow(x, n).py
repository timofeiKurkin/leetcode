class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return x

        if n < 0:
            x = 1 / x
            n = abs(n)

        return x**n


solution = Solution()
print(solution.myPow(x=2.00000, n=10))
print(solution.myPow(x=2.10000, n=3))
print(solution.myPow(x=2.00000, n=-2))
