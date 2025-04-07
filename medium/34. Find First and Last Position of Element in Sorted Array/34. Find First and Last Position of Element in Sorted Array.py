from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # left, right = 0, len(nums) - 1

        # position = [-1, -1]

        # while left <= right:
        #     middle = (left + right) // 2

        #     if nums[middle] == target:
        #         while middle and nums[middle - 1] == target:
        #             middle -= 1

        #         position[0] = middle

        #         while middle <= right and nums[middle] == target:
        #             middle += 1

        #         position[1] = middle - 1
        #         return position

        #     if nums[left] <= nums[middle]:
        #         if nums[left] <= target < nums[middle]:
        #             right = middle - 1
        #         else:
        #             left = middle + 1
        #     else:
        #         if nums[middle] < target <= nums[right]:
        #             left = middle + 1
        #         else:
        #             right = middle - 1

        # return position

        first = self.binarySearch(nums, target, True)
        second = self.binarySearch(nums, target, False)

        return [first, second]

    def binarySearch(self, nums: List[int], target: int, isFirst: bool) -> int:
        low, high = 0, len(nums) - 1
        pos = -1

        while low <= high:
            middle = low + (high - low) // 2
            if nums[middle] == target:
                pos = middle
                if isFirst:
                    high = middle - 1
                else:
                    low = middle + 1
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        return pos


solution = Solution()
print(solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
print(solution.searchRange(nums=[8, 8], target=8))
print(solution.searchRange(nums=[1], target=1))
