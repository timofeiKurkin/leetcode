from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        res = [False] * n
        max_candy = max(candies)

        for i in range(len(res)):
            res[i] = True if candies[i] + extraCandies >= max_candy else False

        return res
