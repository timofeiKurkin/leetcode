import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (math.log(n) / math.log(4)).is_integer()
