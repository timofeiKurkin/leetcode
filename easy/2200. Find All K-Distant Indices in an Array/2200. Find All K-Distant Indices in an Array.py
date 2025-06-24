from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        return self.solution2(nums, key, k)

    def solution1(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        for i, num in enumerate(nums):
            if num == key:
                for j in range(max(0, i - k), min(len(nums), i + k + 1), 1):
                    res.add(j)
        return list(res)

    def solution2(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = set()

        for i, num in enumerate(nums):
            if num == key:
                start = max(0, i - k)
                end = min(n - 1, i + k)
                for j in range(start, end + 1):
                    res.add(j)

        return list(res)


solution = Solution()
print(solution.findKDistantIndices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1))
print(solution.findKDistantIndices(nums=[2, 2, 2, 2, 2], key=2, k=2))
