from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # items = {}
        # for num in nums:
        #     if num not in items:
        #         items[num] = 1
        #     else:
        #         items[num] = items[num] + 1
        # best: float = 0
        # res: int = 0
        # n = len(nums)
        # for item in items.keys():
        #     m: float = items[item] / n
        #     if m > best:
        #         res = item
        #         best = m
        # return res

        # Boyer-Moore Voting Algorithm
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:  # refresh candidate if it's zero
                candidate = num
            count += 1 if candidate == num else -1
        return candidate


solution = Solution()
print(solution.majorityElement([3, 2, 3]))
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
