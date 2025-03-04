from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        best = letters[0]

        for index in range(1, len(letters)):
            current = letters[index]
            if current != target and current > target:
                return current

        return best


letters1 = ["c", "f", "j"]
letters2 = ["c", "f", "j"]
letters3 = ["c", "f", "j"]
letters4 = ["x", "x", "y", "y"]

solution = Solution()
print(solution.nextGreatestLetter(letters1, "a"))
print(solution.nextGreatestLetter(letters2, "c"))
print(solution.nextGreatestLetter(letters3, "d"))
print(solution.nextGreatestLetter(letters4, "z"))
