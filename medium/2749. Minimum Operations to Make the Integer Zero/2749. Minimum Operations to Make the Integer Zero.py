class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1, 61):
            x = num1 - num2 * i

            if x < i:
                return -1
            if i >= x.bit_count():
                return i

        return -1
