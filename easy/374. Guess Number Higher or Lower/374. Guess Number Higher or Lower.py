# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

pick = 0


def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        # nums = [i for i in range(1, n + 1)]

        # while True:
        #     mid = len(nums) // 2
        #     attempt = guess(nums[mid])

        #     if attempt == 0:
        #         return nums[mid]
        #     elif attempt == -1:
        #         nums = nums[:mid]
        #     else:
        #         nums = nums[mid:]

        # if n == 1:
        #     return 1

        # fixed_mid = n // 2 + 1

        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2

            attempt = guess(mid)

            if attempt == 0:
                return mid
            elif attempt == -1:
                right = mid - 1
            else:
                left = mid + 1

        return 0


solution = Solution()
pick = 6
print(solution.guessNumber(n=10))

pick = 1
print(solution.guessNumber(n=1))

pick = 1
print(solution.guessNumber(n=2))

pick = 1702766719
print(solution.guessNumber(n=2126753390))
