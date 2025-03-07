print(12 & 13 & 14 & 15)
print(10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 20)


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # res = left
        # for num in range(left + 1, right + 1):
        #     res &= num
        #     if res:
        #         return res
        # return res

        shift_count = 0
        while left != right and left > 0:
            shift_count += 1
            left >>= 1
            right >>= 1

        return left << shift_count


solution = Solution()
print(solution.rangeBitwiseAnd(left=5, right=7))
print(solution.rangeBitwiseAnd(left=0, right=0))
print(solution.rangeBitwiseAnd(left=12, right=15))
print(solution.rangeBitwiseAnd(left=1, right=2147483647))
