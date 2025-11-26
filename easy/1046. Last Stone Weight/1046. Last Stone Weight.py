import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)

        while len(stones) >= 2:
            y = abs(heapq.heappop(stones))
            x = abs(heapq.heappop(stones))

            if x != y:
                heapq.heappush(stones, (y - x) * -1)

        return abs(heapq.heappop(stones)) if len(stones) else 0
