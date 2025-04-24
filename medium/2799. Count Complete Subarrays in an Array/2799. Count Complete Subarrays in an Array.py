from collections import defaultdict
from typing import List, Set


def is_valid_subarray(items: Set[int], array: List[int]) -> bool:
    # items_set = set()
    # for num in array:
    #     if num not in items_set:
    #         items_set.add(num)
    # return len(items_set) == target

    for key in items:
        if key not in array:
            return False
    return True


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # for num in nums:
        #     if num not in nums_set:
        #         nums_set.add(num)

        # Recursion
        # def run(array: List[int]) -> List[int]:
        #     if not array or not is_valid_subarray(array, nums_set):
        #         return []

        #     return run(array[1:]) + [array] + run(array[1:-1])

        # res = run(nums)
        # print(res)
        # return len(res)

        # Sliding window
        # k = len(nums_set)
        # n = len(nums)
        # subarrays = []

        # while second <= n:
        #     curr_arr = nums[first:second]
        #     if not is_valid_subarray(curr_arr, nums_set):
        #         second += 1
        #         first = max(0, first - 1)
        #         continue

        #     first += 1
        #     subarrays.append(curr_arr)

        # # The count of unique nums in list
        # nums_set: Set[int] = set(nums)

        # # Sliding window
        # n = len(nums)
        # subarrays = 0

        # for i in range(n + 1):
        #     for j in range(i + 1, n + 1):
        #         if set(nums[i:j]) == nums_set:
        #             subarrays += 1

        # return subarrays

        total_unique, n = len(set(nums)), len(nums)
        total = 0
        freq = defaultdict(int)
        l = 0

        for r in range(n):
            freq[nums[r]] += 1

            while len(freq) == total_unique:
                total += n - r
                freq[nums[l]] -= 1
                if not freq[nums[l]]:
                    del freq[nums[l]]
                left += 1

        return total


solution = Solution()
print(solution.countCompleteSubarrays(nums=[1, 3, 1, 2, 2]))
print(solution.countCompleteSubarrays(nums=[5, 5, 5, 5]))
print(solution.countCompleteSubarrays(nums=[1, 3, 2, 4, 6, 2, 1, 4, 2, 3, 1]))
print(solution.countCompleteSubarrays(nums=[42]))
print(solution.countCompleteSubarrays(nums=[1, 2, 3, 4, 5]))
print(solution.countCompleteSubarrays(nums=[1, 2, 3, 1, 2, 4, 5, 6]))
print(solution.countCompleteSubarrays(nums=[5, 4, 3, 2, 1, 5, 4, 3, 2, 1]))
print(solution.countCompleteSubarrays(nums=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(solution.countCompleteSubarrays(nums=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]))
print(solution.countCompleteSubarrays(nums=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(solution.countCompleteSubarrays(nums=[1, 2, 1, 3, 1, 4, 1, 5, 1]))
print(solution.countCompleteSubarrays(nums=[1, 1, 2, 2, 3, 3, 4, 4, 5]))
print(solution.countCompleteSubarrays(nums=[999, 1000, 999, 1000, 999]))
print(solution.countCompleteSubarrays(nums=[1, 2, 3, 2, 1]))
print(solution.countCompleteSubarrays(nums=[3, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]))
