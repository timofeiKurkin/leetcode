from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # res: List[int] = []

        # is_going_right = True
        # is_going_left = False
        # is_going_down = False
        # is_going_top = False

        # top = 0
        # bottom = len(matrix) - 1
        # left = 0
        # right = len(matrix[0]) - 1

        # while top <= bottom and left <= right:
        #     if is_going_right:
        #         items = matrix[top][left : right + 1]
        #         res += items
        #         top += 1

        #         is_going_right = False
        #         is_going_down = True

        #     elif is_going_down:
        #         items = [item[right] for item in matrix[top : bottom + 1]]
        #         res += items

        #         right -= 1

        #         is_going_down = False
        #         is_going_left = True
        #     elif is_going_left:
        #         items = matrix[bottom][left : right + 1]
        #         items.reverse()
        #         res += items

        #         bottom -= 1

        #         is_going_left = False
        #         is_going_top = True
        #     elif is_going_top:
        #         items = [item[left] for item in matrix[top : bottom + 1]]
        #         items.reverse()
        #         res += items

        #         left += 1

        #         is_going_top = False
        #         is_going_right = True

        # return res

        res = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right =len(matrix[0]) - 1
        direction_index = 0  # 0 - вправо; 1 - вниз; 2 - влево; 3 - вверх

        while top <= bottom and left <= right:
            if direction_index == 0:
                res.extend(matrix[top][left : right + 1])
                top += 1
            elif direction_index == 1:
                res.extend(matrix[i][right] for i in range(top, bottom + 1))
                right -= 1
            elif direction_index == 2:
                res.extend(matrix[bottom][left : right + 1][::-1])
                bottom -= 1
            elif direction_index == 3:
                res.extend(matrix[i][left] for i in range(bottom, top - 1, -1))
                left += 1

            direction_index = (direction_index + 1) % 4

        return res


solution = Solution()
print(solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(
    solution.spiralOrder(
        [[1, 2, 3, 4], [5, 6, 7, 8], [12, 23, 34, 45], [9, 10, 11, 12]]
    )
)

# [1, 2, 3, 4, 8, 45, 12, 11, 10, 9, 5, 12, 6, 7, 34, 23]
# [1, 2, 3, 4, 8, 45, 12, 11, 10, 9, 12, 5, 6, 7, 34, 23] - leetcode
