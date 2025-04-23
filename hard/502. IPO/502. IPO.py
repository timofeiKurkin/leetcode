import heapq
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))

        n = len(profits)
        # items = [[profits[i], capital[i]] for i in range(n)]
        items = [i for i in range(n)]
        print(items)
        items.sort(key=lambda x: capital[x])

        print(items)

        pq = []

        def put(val: int):
            heapq.heappush(pq, -val)

        def get():
            return -heapq.heappop(pq)

        idx = 0
        for _ in range(k):
            while idx < n and capital[items[idx]] <= w:
                put(profits[items[idx]])
                idx += 1

            if not pq:
                break

            w += get()

        return w


solution = Solution()
# solution.findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1])
# solution.findMaximizedCapital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2])
