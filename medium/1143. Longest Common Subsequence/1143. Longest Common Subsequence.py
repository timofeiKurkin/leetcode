class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # dp[1][1] = 1 if text1[0] == text2[0] else 0

        # for i in range(1, m):
        #     dp[i][0] = dp[i - 1][0]
        #     if text2[0] == text1[i]:
        #         dp[i][0] += 1

        # for j in range(1, n):
        #     dp[0][j] = dp[0][j - 1]
        #     if text1[0] == text2[j]:
        #         dp[0][j] += 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # If symbols match, take diagonal + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Take maximum from prev vertical or horizontal
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # print(dp)
        return dp[m][n]


solution = Solution()
print(solution.longestCommonSubsequence(text1="abcde", text2="ace"))  # 3
print(solution.longestCommonSubsequence(text1="abc", text2="abc"))  # 3
print(solution.longestCommonSubsequence(text1="abc", text2="def"))  # 0
print(solution.longestCommonSubsequence(text1="aggtab", text2="gxtxayb"))  # 4

# [
# [0, 0, 0, 0, 1, 1, 1],
# [1, 1, 1, 1, 1, 1, 1],
# [2, 2, 2, 2, 2, 2, 2],
# [2, 2, 3, 3, 3, 3, 3],
# [2, 2, 3, 3, 4, 4, 4],
# [2, 2, 3, 3, 4, 4, 5]
# ]
