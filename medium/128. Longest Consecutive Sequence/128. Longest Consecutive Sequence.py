from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums or len(nums) == 1:
        #     return len(nums)
        # # It is wrong to use .sort()
        # nums.sort()
        # prev = nums[0]
        # count = [1]
        # for num in nums[1:]:
        #     if prev == num:
        #         continue
        #     if abs(num - prev) == 1:
        #         count[-1] += 1
        #     else:
        #         count.append(1)
        #     prev = num
        # return max(*count) if len(count) > 1 else count[0]

        if not nums:
            return 0

        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length


solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
