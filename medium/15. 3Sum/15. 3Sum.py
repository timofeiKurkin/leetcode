from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorted_nums = sorted(nums)
        # i = 0
        # right = 1
        # last = -1
        # while i < len(sorted_nums):
        #     right_num = sorted_nums[right]
        #     last_num = sorted_nums[last]
        #     curr_num = sorted_nums[i]

        #     if curr_num == sorted_nums[i - 1]:
        #         i += 1
        #         continue
        #     elif right_num == last_num:
        #         right -= 1

        #     if (
        #         curr_num != right_num
        #         and curr_num != last_num
        #         and last_num != right_num
        #         and curr_num != sorted_nums[i - 1]
        #     ):
        #         if right_num + last_num + curr_num == 0:
        #             res.append([right_num, last_num, curr_num])
        #             right -= 1
        #             last += 1
        #             i += 1
        #         elif right + last + curr_num > 0:
        #             right -= 1
        #         elif right + last + curr_num < 0:
        #             last += 1
        #     else:
        #         i += 1
        #         right -= 1
        #         last += 1

        nums.sort()
        res: List[List[int]] = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            right = len(nums) - 1
            left = i + 1

            while left < right:
                total = nums[i] + nums[right] + nums[left]

                if total > 0:
                    right -= 1
                if total < 0:
                    left += 1
                if total == 0:
                    res.append([nums[i], nums[right], nums[left]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
