from typing import List, Tuple


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        new_nums: List[Tuple[int, int]] = []

        for i in range(n):
            new_nums.append((nums[i], i))

        new_nums.sort(key=lambda x: x[0])
        return list(map(lambda x: x[0], sorted(new_nums[-k:], key=lambda x: x[1])))


solution = Solution()
print(solution.maxSubsequence(nums=[2, 1, 3, 3], k=2))
print(solution.maxSubsequence(nums=[-1, -2, 3, 4], k=3))
print(solution.maxSubsequence(nums=[3, 4, 3, 3], k=2))
print(solution.maxSubsequence(nums=[63, -74, 61, -17, -55, -59, -10, 2, -60, -65], k=9))
