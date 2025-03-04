from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1  # for nums1
        b = n - 1  # for nums2
        c = m + n - 1  # for finished array

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[c] = nums1[a]
                a -= 1
            elif a < 0 or nums2[b] >= nums1[a]:
                nums1[c] = nums2[b]
                b -= 1
            c -= 1
