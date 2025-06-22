from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        for i in range(0, len(s), k):
            res.append(s[i : i + k])
        res[-1] += fill * (k - len(res[-1]))
        return res
