from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % 2 == 0:
                    res += 1

        return res


solution = Solution()
print(solution.countPairs(nums=[3, 1, 2, 2, 2, 1, 3], k=2))
print(solution.countPairs(nums=[1, 2, 3, 4], k=1))
