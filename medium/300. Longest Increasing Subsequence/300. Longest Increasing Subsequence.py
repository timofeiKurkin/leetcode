from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp: List[int] = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


solution = Solution()
print(solution.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(solution.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))  # 4
print(solution.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))  # 1
print(solution.lengthOfLIS(nums=[-2, -1]))  # 2
print(solution.lengthOfLIS(nums=[10, 9, 2, 5, 3, 4]))  # 3
print(solution.lengthOfLIS(nums=[1, 2, 3, 4]))  # 3
