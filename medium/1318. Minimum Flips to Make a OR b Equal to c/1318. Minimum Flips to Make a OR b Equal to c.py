class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        while a or b or c:
            if c % 2 == 1:
                flips += int(not (a % 2 or b % 2))
            else:
                flips += int(a % 2) + int(b % 2)

            a //= 2
            b //= 2
            c //= 2

        return flips


solution = Solution()
print(solution.minFlips(1, 4, 5))
