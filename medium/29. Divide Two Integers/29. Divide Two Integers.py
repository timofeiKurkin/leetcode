class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        if MIN_INT == dividend and divisor == -1:
            return MAX_INT

        sign = 1 if dividend * divisor >= 0 else -1

        a = abs(dividend)
        b = abs(divisor)
        res = 0

        while (a - b) >= 0:
            x = 0  # 2^0 = 1
            while a - (b << 1 << x) >= 0:
                x += 1

            res += 1 << x
            a -= b << x

        return res * sign
