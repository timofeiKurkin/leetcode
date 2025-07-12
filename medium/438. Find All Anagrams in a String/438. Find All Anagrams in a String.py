from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        return self.solution2(s, p)

    def solution1(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        ht = defaultdict(list)

        for i in range((n - m) + 1):
            key = tuple(sorted(list(s[i : i + m])))
            ht[key].append(i)

        return ht[tuple(sorted(list(p)))]

    def solution2(self, s: str, p: str) -> List[int]:
        m = len(p)
        pp = sorted(p)
        res = []

        for i in range((len(s) - m) + 1):
            if sorted(p[i : i + m]) == pp:
                res.append(i)

        return res
