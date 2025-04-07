from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # def findInt(items: List[int], index_start: int) -> int:
        #     if not items or len(items) == 1 and items[0] != target:
        #         return -1

        #     if items[0] == target:
        #         return index_start
        #     elif items[-1] == target:
        #         return index_start + len(items) - 1

        #     middle = len(items) // 2

        #     if items[middle] == target:
        #         return middle + index_start

        #     right_side_center = items[middle + len(items[middle:]) // 2]
        #     left_side_center = items[middle - len(items[: middle + 1]) // 2]

        #     if abs(target - right_side_center) <= abs(target - left_side_center):
        #         return findInt(items[middle:], index_start + middle)
        #     else:
        #         return findInt(items[:middle], index_start)

        # return findInt(nums, 0)

        # if nums()

        if abs(target - nums[-1]) <= abs(target - nums[0]):
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == target:
                    return i
                if nums[i] < target:
                    return -1
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                if nums[i] > target:
                    return -1

        return -1


solution = Solution()
print(solution.search(nums=[1], target=1))  # 0
print(solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))  # 4
print(solution.search(nums=[5, 6, 7, 0, 1, 2], target=0))  # 3
print(solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))  # -1
print(solution.search(nums=[1], target=0))  # -1
print(solution.search(nums=[1, 3, 5], target=5))  # 2
print(solution.search(nums=[1, 3], target=1))  # 0
print(solution.search(nums=[5, 1, 3], target=5))  # 0
print(solution.search(nums=[9, 1, 2, 3, 4, 5, 6, 7, 8], target=9))  # 0
print(solution.search(nums=[9, 1, 2, 3, 4, 5, 6, 7, 8], target=8))  # 8
print(
    solution.search(
        nums=[
            57,
            58,
            59,
            62,
            63,
            66,
            68,
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            80,
            81,
            86,
            95,
            96,
            97,
            98,
            100,
            101,
            102,
            103,
            110,
            119,
            120,
            121,
            123,
            125,
            126,
            127,
            132,
            136,
            144,
            145,
            148,
            149,
            151,
            152,
            160,
            161,
            163,
            166,
            168,
            169,
            170,
            173,
            174,
            175,
            178,
            182,
            188,
            189,
            192,
            193,
            196,
            198,
            199,
            200,
            201,
            202,
            212,
            218,
            219,
            220,
            224,
            225,
            229,
            231,
            232,
            234,
            237,
            238,
            242,
            248,
            249,
            250,
            252,
            253,
            254,
            255,
            257,
            260,
            266,
            268,
            270,
            273,
            276,
            280,
            281,
            283,
            288,
            290,
            291,
            292,
            294,
            295,
            298,
            299,
            4,
            10,
            13,
            15,
            16,
            17,
            18,
            20,
            22,
            25,
            26,
            27,
            30,
            31,
            34,
            38,
            39,
            40,
            47,
            53,
            54,
        ],
        target=30,
    )
)  # 113
