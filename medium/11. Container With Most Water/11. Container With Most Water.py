from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        square = 0

        while l < r:
            square = max(square, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return square


solution = Solution()

height_1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height_2 = [1, 1]

print(solution.maxArea(height_1))
# print(solution.maxArea(height_2))
