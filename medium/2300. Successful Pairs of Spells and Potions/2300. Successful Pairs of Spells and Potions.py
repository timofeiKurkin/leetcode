from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        res = []

        for s in spells:
            biggest = potions[-1] * s

            if biggest < success:
                res.append(0)
                continue

            left, right = 0, len(potions) - 1

            while left < right:
                mid = left + (right - left) // 2
                if potions[mid] * s > success:
                    right = mid
                else:
                    left = mid + 1

            res.append(len(potions) - left)

        return res


solution = Solution()
print(solution.successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
