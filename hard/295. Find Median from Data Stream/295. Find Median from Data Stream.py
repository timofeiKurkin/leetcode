import heapq
from typing import List


class MedianFinder:

    def __init__(self):
        self.max_pq: List[int] = []
        self.min_pq: List[int] = []
        self.middle = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_pq, -num)
        heapq.heappush(self.min_pq, -heapq.heappop(self.max_pq))

        if len(self.min_pq) > len(self.max_pq):
            heapq.heappush(self.max_pq, -heapq.heappop(self.min_pq))

    def findMedian(self) -> float:
        if len(self.min_pq) == len(self.max_pq):
            return (-self.max_pq[0] + self.min_pq[0]) / 2
        return -self.max_pq[0]
