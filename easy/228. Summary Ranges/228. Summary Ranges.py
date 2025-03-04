from typing import List


class Solution:
    def create_diapason(self, diapason: List[str]) -> str:
        if len(diapason) > 1:
            return f"{diapason[0]}->{diapason[-1]}"
        return diapason[0]

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        res: List[str] = []
        diapason: List[str] = [str(nums[0])]

        for i in range(1, len(nums)):
            curr = nums[i]

            if int(diapason[-1]) + 1 == curr:
                diapason.append(str(curr))
            else:
                res.append(self.create_diapason(diapason))
                diapason = [str(curr)]

        if len(diapason):
            res.append(self.create_diapason(diapason))

        return res


solution = Solution()
print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))
print(solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
