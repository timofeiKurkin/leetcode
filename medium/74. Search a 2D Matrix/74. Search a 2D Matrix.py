from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(arr: List[int], low: int, high: int, target: int) -> bool:
            if high >= low:
                mid = (high + low) // 2

                if arr[mid] == target:
                    return True

                elif arr[mid] > target:
                    return binary_search(arr, low, mid - 1, target)
                else:
                    return binary_search(arr, mid + 1, high, target)
            else:
                return False

        for i in range(len(matrix)):
            res = binary_search(matrix[i], 0, len(matrix[0]) - 1, target)

            if res:
                return res

        return False


solution = Solution()

print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
