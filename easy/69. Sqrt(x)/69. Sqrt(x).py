import math


class Solution:
    def mySqrt(self, x: int) -> int:
        # To solve this problem we should use Heron's Alogrithm
        # Formula: X n+1 = 1/2 * (X n + A / X n)
        # Heron's Alog is iterative and takes an approximate value and returns a new approximate value which is less then the previous one.
        # This can be repeated over and over until the desired accuracy is reached.
        # You can get more info: https://medium.com/@gauravswarankar/heron-algorithm-or-babylonian-method-square-root-14fb599db5d7

        x_n = x / 2
        diff = 1
        accuracy = 0.01

        while diff > accuracy:
            x_n1 = 0.5 * (x_n + x / x_n)
            diff = x_n - x_n1
            x_n = x_n1

        return math.floor(x_n)


solution = Solution()
print(solution.mySqrt(4))
print(solution.mySqrt(8))
