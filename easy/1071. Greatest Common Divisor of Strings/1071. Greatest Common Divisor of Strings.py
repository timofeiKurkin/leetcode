import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if str1[0] != str2[0]:
        #     return ""

        # # Take the longest and the smallest strings
        # # Use the smallest string as a prefix
        # if len(str1) == len(str2):
        #     s = str1
        #     t = str2
        # else:
        #     s = max(str1, str2, key=len)  # i
        #     t = min(str1, str2, key=len)  # j
        # n = len(t)

        # while n:
        #     p = t[:n]
        #     i, j = 0, 0

        #     while i < len(s) or j < len(t):
        #         if s[i : i + n] == p and t[j : j + n] == p:
        #             i += n
        #             j += n
        #         else:
        #             break

        #     if j < len(t) or i > len(s) or j > len(s):
        #         n -= 1
        #         continue

        #     if j == len(t) and i != len(s):
        #         while i < len(s):
        #             if s[i : i + n] == p:
        #                 i += n
        #             else:
        #                 n -= 1
        #                 break

        #     if i == len(s) and j == len(t):
        #         return p

        # return ""

        if str1 + str2 != str2 + str1:
            return ""
        m = math.gcd(len(str1), len(str2))
        return str1[:m]


solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))
print(solution.gcdOfStrings("ABABAB", "ABAB"))
print(solution.gcdOfStrings("LEET", "CODE"))
print(solution.gcdOfStrings("GABCABC", "ABC"))
print(
    solution.gcdOfStrings(
        "TAUXXTAUXXTAUXXTAUXXTAUXX",
        "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX",  # "TAUXX" || "TAUXXTAUXXTAUXX"
    )
)
