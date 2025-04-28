# from collections import deque
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # res = 0
        # left, right = 0, 0
        # curr_sum = 0
        # length = 0

        # while right < len(nums):
        #     num = nums[right]

        #     if num > k:
        #         left = 0
        #         curr_sum = 0
        #         length = 0
        #         continue

        #     if (curr_sum + num) * (length + 1) < k:
        #         curr_sum += num
        #         length += 1
        #         res += max(0, right - left + 1)
        #         right += 1
        #     else:
        #         curr_sum -= nums[left]
        #         length -= 1
        #         left += 1

        # return res

        # res = 0
        # curr_sum = 0
        # left = 0
        # length = 0

        # for right in range(len(nums)):
        #     num = nums[right]

        #     if num > k:
        #         left = right
        #         curr_sum = 0
        #         length = 0
        #         continue

        #     if (curr_sum + num) * (length + 1) < k:
        #         curr_sum += num
        #         res += max(0, right - left + 1)
        #         length += 1

        left = 0
        curr_sum = 0
        length = 0
        res = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum * (right - left + 1) >= k:
                curr_sum -= nums[left]
                left += 1

            res += max(0, right - left + 1)

        return res


solution = Solution()
print(solution.countSubarrays(nums=[2, 1, 4, 3, 5], k=10))  # 6
print(solution.countSubarrays(nums=[1, 1, 1], k=5))  # 5
print(solution.countSubarrays(nums=[5, 2, 6, 8, 9, 7], k=50))  # 13
