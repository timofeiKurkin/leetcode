from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums) // 2

        return self.binary_search(nums[:n], target, True) or self.binary_search(
            nums[n:], target, False
        )

    def binary_search(self, nums: List[int], target: int, ifForward: bool) -> bool:
        start = 0 if ifForward else len(nums) - 1
        end = len(nums) if ifForward else -1
        step = 1 if ifForward else -1

        for i in range(start, end, step):
            if nums[i] == target:
                return True

        return False


solution = Solution()
# print(solution.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
# print(solution.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))
# print(solution.search(nums=[1, 0, 1, 1, 1], target=0))
print(
    solution.search(
        nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], target=2
    )
)
# print(
#     solution.search(
#         nums=[1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], target=2
#     )
# )
