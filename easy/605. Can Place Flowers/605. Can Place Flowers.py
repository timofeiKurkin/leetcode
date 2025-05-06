import math
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return not flowerbed[0]

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1

        for i in range(1, len(flowerbed) - 1):
            if not n:
                return True

            if flowerbed[i - 1] == 1:
                continue
            elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] != 1:
                flowerbed[i] = 1
                n -= 1

        return not bool(n)


print(round(3 / 2))
print(math.floor(3 / 2))
print(3 // 2)
