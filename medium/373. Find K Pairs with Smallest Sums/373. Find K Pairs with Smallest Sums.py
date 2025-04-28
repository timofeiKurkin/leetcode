import heapq
from typing import List, Tuple


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        # TLE
        # freq = defaultdict(list)
        # pq = []
        # for i, u in enumerate(nums1):
        #     if len(pq) > k:
        #             break
        #     for j, v in enumerate(nums2):
        #         if len(pq) > k:
        #             break
        #         curr_sum = u + v
        #         heapq.heappush(pq, curr_sum)
        #         freq[curr_sum].append([u, v])
        # res = []
        # for _ in range(k):
        #     key = heapq.heappop(pq)
        #     res.append(freq[key].pop())
        #     if not freq[key]:
        #         del freq[key]
        # return res

        res = []

        # Save
        pq: List[Tuple[int]] = []

        for j in range(min(k, len(nums2))):
            heapq.heappush(pq, (nums1[0] + nums2[j], 0, j))

        while pq and len(res) < k:
            _, i, j = heapq.heappop(pq)
            res.append([nums1[i], nums2[j]])

            if i < len(nums1):
                heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))

        return res
