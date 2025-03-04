from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans: List[int] = []

        for i in range(n + 1):
            ans.append(self.countBitsInANum(i))

        return ans

    def countBitsInANum(self, num: int) -> int:
        ans = 0

        while num > 0:
            ans += num & 1
            num //= 2

        return ans
