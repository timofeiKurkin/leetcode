from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        items1 = set(nums1)
        items2 = set(nums2)

        return [
            list(filter(lambda x: x not in items2, items1)),
            list(filter(lambda x: x not in items1, items2)),
        ]
