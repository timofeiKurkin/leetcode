from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(key=lambda x: x, reverse=True)

        for i, num in enumerate(citations[:-1]):
            if num > i and citations[i + 1] <= i + 1:
                return i + 1

        return len(citations) if citations[0] else 0


solution = Solution()
print(solution.hIndex([3, 0, 6, 1, 5]))
print(solution.hIndex([1, 3, 1]))
print(solution.hIndex([1, 2, 3]))
print(solution.hIndex([0]))
print(solution.hIndex([4]))
