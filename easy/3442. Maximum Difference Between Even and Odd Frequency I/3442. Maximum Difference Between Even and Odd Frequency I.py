from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(list(s))

        max_odd = 0
        min_even = 10**10
        for _, v in cnt.items():
            if v % 2 != 0 and v > max_odd:
                max_odd = v

            if v % 2 == 0 and v < min_even:
                min_even = v

        return max_odd - min_even


solution = Solution()
print(solution.maxDifference(s="aaaaabbc"))
print(solution.maxDifference(s="abcabcab"))
