import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        hp = []

        comb = sorted(list(zip(nums1, nums2)), key=lambda x: x[1], reverse=True)

        for num1, num2 in comb:
            prefix_sum += num1
            heapq.heappush(hp, num1)

            if len(hp) == k:
                res = max(res, prefix_sum * num2)
                prefix_sum -= heapq.heappop(hp)

        return res
