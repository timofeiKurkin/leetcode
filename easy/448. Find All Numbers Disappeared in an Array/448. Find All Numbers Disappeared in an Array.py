from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        res: List[int] = []

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res


solution = Solution()

print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(solution.findDisappearedNumbers([1, 1]))
print(solution.findDisappearedNumbers([1, 1, 3]))
