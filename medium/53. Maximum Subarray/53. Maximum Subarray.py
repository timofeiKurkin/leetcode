from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Глобальный результат подсчета
        res = nums[0]

        # Максимальная сумма элементов до тех пор, пока не будет найден наибольший i элемент
        max_ending = nums[0]
        n = len(nums)

        for i in range(1, n):
            max_ending = max(max_ending + nums[i], nums[i])
            res = max(res, max_ending)

        return res
