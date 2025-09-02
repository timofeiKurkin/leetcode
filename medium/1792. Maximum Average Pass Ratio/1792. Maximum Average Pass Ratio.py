import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        average_sum = 0
        hp = []

        for p, q in classes:
            average_sum += p / q
            increment = (p - q) / (q * (q + 1))
            heapq.heappush(hp, (increment, p, q))

        for _ in range(extraStudents):
            (increment, p, q) = hp[0]

            if not increment:
                break

            average_sum -= increment
            new_increment = (p - q) / ((q + 1.0) * (q + 2.0))
            heapq.heapreplace(hp, (new_increment, p + 1, q + 1))

        return average_sum / n
