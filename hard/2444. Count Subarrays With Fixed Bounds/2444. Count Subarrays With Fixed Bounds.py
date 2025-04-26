from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # n = len(nums)
        # res = 0

        # for left in range(n):
        #     items = set()
        #     isReady = False

        #     for right in range(left, n):
        #         if nums[right] > maxK or nums[right] < minK:
        #             break

        #         items.add(nums[right])

        #         if isReady:
        #             res += 1
        #         elif minK in items and maxK in items:
        #             res += 1
        #             isReady = True

        # return res

        worst = -1
        last_min = -1
        last_max = -1
        res = 0

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                worst = i

            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i

            res += max(0, min(last_min, last_max) - worst)

        return res


solution = Solution()
print(solution.countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5))
print(solution.countSubarrays(nums=[1, 1, 1, 1], minK=1, maxK=1))
