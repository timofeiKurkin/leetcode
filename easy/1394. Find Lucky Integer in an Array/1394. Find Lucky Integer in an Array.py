from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        res = -1

        for k, v in cnt.items():
            if k == v:
                res = max(res, v)

        return res
