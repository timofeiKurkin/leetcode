from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # numsObj = {}
        # for num in nums:
        #     if num in numsObj:
        #         numsObj[num] = numsObj[num] + 1
        #     else:
        #         numsObj[num] = 1
        # for item in numsObj.items():
        #     print(item)
        #     if item[1] == 1:
        #         return item[0]

        ones, twos = 0, 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            common_mask = ~(ones & twos)
            ones &= common_mask
            twos &= common_mask
        return ones
        

solution = Solution()
print(solution.singleNumber([2, 2, 3, 2]))
print(solution.singleNumber([0, 1, 0, 1, 0, 1, 99]))
