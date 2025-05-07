from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # n = len(nums)
        # if n < 3:
        #     return False

        # items: List[int] = [nums[0]]

        # for i in range(1, n):

        #     if nums[i] > items[-1] and len(items) < 3:
        #         items.append(nums[i])
        #     else:
        #         items = items[1:] + [nums[i]]

        #     if len(items) ==

        # print(items)
        # return len(items) == 3

        first_item = float("inf")
        second_item = float("inf")

        for num in nums:
            if num <= first_item:
                first_item = num
            elif num <= second_item:
                second_item = num
            else:
                return True

        return False
