from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        return self.solution2(fruits, baskets)

    def solution1(self, fruits: List[int], baskets: List[int]) -> int:
        # Brute-force solution
        unplaced = 0

        for fruit in fruits:
            placed = False

            for i, basket in enumerate(baskets):
                if fruit <= basket:
                    placed = True
                    baskets.pop(i)
                    break

            if not placed:
                unplaced += 1

        return unplaced

    def solution2(self, fruits: List[int], baskets: List[int]) -> int:
        # Segment Tree
        placed = len(fruits)

        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if fruit <= basket:
                    placed -= 1
                    baskets[i] = 0
                    break

        return placed
