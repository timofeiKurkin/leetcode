from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(mid: int) -> bool:
            return sum(map(lambda x: (x + mid - 1) // mid, piles)) <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2  # The new speed to eat bananas

            if can_eat_all(mid):
                right = mid
            else:
                left = mid + 1

        return left


solution = Solution()
print(solution.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))


# piles = [3, 6, 7, 11]; k = 4; h = 8
# [0, 6, 7, 11] h = 7
# [0, 2, 7, 11] h = 6
# [0, 0, 7, 11] h = 5
# [0, 0, 3, 11] h = 4
# [0, 0, 0, 11] h = 3
# [0, 0, 0, 7]  h = 2
# [0, 0, 0, 3] h = 1
# [0, 0, 0, 0] h = 0
