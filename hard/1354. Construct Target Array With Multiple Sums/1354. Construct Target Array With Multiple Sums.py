import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        prev_sum = sum(target)
        target = [-t for t in target]
        heapq.heapify(target)

        while True:
            t = heapq.heappop(target) * -1
            prev_sum -= t

            if t == 1 or prev_sum == 1:
                return True

            if t < prev_sum or not prev_sum or not t % prev_sum:
                return False

            t %= prev_sum
            prev_sum += t
            heapq.heappush(target, t * -1)


solution = Solution()

print(solution.isPossible([9, 3, 5]))
print(solution.isPossible([1, 1, 1, 2]))
print(solution.isPossible([8, 5]))
