import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.solution2(nums, k)

    def solution1(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        items = list(cnt.items())
        items.sort(key=lambda x: x[1], reverse=True)
        return list(map(lambda x: x[0], items[:k]))

    def solution2(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        hp = []

        for item in cnt.items():
            # print(item)
            # heapq.heappush(hp, (item[1], item[0]))

            # while len(hp) > k:
            #     heapq.heap

            key = (item[1], item[0])
            if len(hp) == 2:
                heapq.heappushpop(hp, key)
            else:
                heapq.heappush(hp, key)

        return list(map(lambda x: x[1], hp))


solution = Solution()
print(solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
