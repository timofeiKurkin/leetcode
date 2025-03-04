from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            exact_diff = target - num

            if exact_diff in seen:
                return [seen[exact_diff], i + 1]

            if num not in seen:
                seen[num] = i + 1

        return seen


numbers_1 = [2, 7, 11, 15]
numbers_2 = [2, 3, 4]
numbers_3 = [-1, 0]

solution = Solution()

print(solution.twoSum(numbers_1, 9))
print(solution.twoSum(numbers_2, 6))
print(solution.twoSum(numbers_3, -1))
