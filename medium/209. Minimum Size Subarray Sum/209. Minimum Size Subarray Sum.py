from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        left = 0
        min_length = float("inf")
        window_sum = 0

        for right in range(n):
            window_sum += nums[right]

            while window_sum >= target:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return min_length if min_length != float("inf") else 0


solution = Solution()
print(solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(solution.minSubArrayLen(target=4, nums=[1, 4, 4]))
print(solution.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
print(solution.minSubArrayLen(target=11, nums=[1, 2, 3, 4, 5]))


# print([1, 2, 3, 4, 5][0:0])
# print([1, 2, 3, 4, 5][0:1])
