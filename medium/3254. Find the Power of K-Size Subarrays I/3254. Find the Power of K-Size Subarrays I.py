from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # res: List[int] = []

        # def run(nums: List[int]) -> None:
        #     nonlocal res

        #     if len(nums) < k:
        #         return

        #     sub_array: List[int] = nums[:k]
        #     is_power = self.check_power(sub_array)
        #     res.append(sub_array.pop() if is_power else -1)

        #     run(nums[1:])

        # run(nums)
        # return res

        if len(nums) < k:
            return

        sub_array: List[int] = nums[:k]
        is_power = self.check_power(sub_array)
        max_num = sub_array.pop() if is_power else -1
        next_num = self.resultsArray(nums[1:], k) or []

        return [max_num, *next_num]

    def check_power(self, nums: List[int]) -> bool:
        for i in range(0, len(nums) - 1, 1):
            if nums[i + 1] - nums[i] != 1:
                return False

        return True
