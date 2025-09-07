from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        return self.solution2(n)

    def solution1(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        if n % 2 == 0:
            items = []

            for i in range(-(n // 2), n // 2 + 1):
                if i:
                    items.append(i)

            return items
        else:
            positive = list(range(1, n))
            return [-sum(positive)] + positive

    def solution2(self, n: int) -> List[int]:
        return [n * (1 - n) // 2] + list(range(1, n))
