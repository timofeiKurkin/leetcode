from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        first = second = 0
        n = len(nums1) + len(nums2)
        middle = n // 2

        for _ in range(middle + 1):
            first = second
            if i < len(nums1) and (j >= len(nums2) or nums1[i] < nums2[j]):
                second = nums1[i]
                i += 1
            else:
                second = nums2[j]
                j += 1

        if n % 2 == 0:
            return (first + second) / 2
        return second


solution = Solution()
print(solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))  # 2
print(solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))  # 2.5
print(solution.findMedianSortedArrays(nums1=[1, 2, 3], nums2=[4, 5, 6]))  # 3.5
print(solution.findMedianSortedArrays(nums1=[1, 2, 6], nums2=[3, 4, 5]))  # 3.5
print(solution.findMedianSortedArrays(nums1=[2], nums2=[1, 3, 4]))  # 2.5
