from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.solution1(nums)

    def solution1(self, nums: List[int]) -> int:
        my_set: set[int] = set()
        for num in nums:
            if num in my_set:
                return num
            my_set.add(num)

        return -1

    def solution2(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow]

        return slow


solution = Solution()
print(solution.findDuplicate([1, 3, 4, 2, 2]))
