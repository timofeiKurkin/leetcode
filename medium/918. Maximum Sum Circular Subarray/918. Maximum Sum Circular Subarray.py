from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Использовать алгоритм Каданэ
        # https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
        def kadane(arr: List[int]) -> int:
            max_ending = res = arr[0]
            for num in arr[1:]:
                max_ending = max(num, max_ending + num)
                res = max(res, max_ending)
            return res

        # Максимальная сумма обычного под массива без учета цикличности
        normalMaxSum = kadane(nums)

        # Если сумма отрицательная, вернуть значение и не продолжать подсчет
        if normalMaxSum < 0:
            return normalMaxSum

        totalSum = sum(nums)  # Общая сумма всех элементов массива
        invert_nums = [-num for num in nums]  # Инвертировать значения массива
        minSubarraySum = kadane(invert_nums)  # Вычислить минимальную сумму массива
        circularMaxSum = (
            totalSum + minSubarraySum
        )  # Вычислить максимальную сумму "циркулярного" массива

        return max(circularMaxSum, normalMaxSum)  # Выбрать то, что больше


solution = Solution()
print(solution.maxSubarraySumCircular([1, -2, 3, -2]))  # 3
print(solution.maxSubarraySumCircular([5, -3, 5]))  # 10
print(solution.maxSubarraySumCircular([-3, -2, -3]))  # -2
print(solution.maxSubarraySumCircular([5, -3, 5, -2, 5]))  # 13
print(solution.maxSubarraySumCircular([-1, 1, -2, 3, 2]))  # 5
