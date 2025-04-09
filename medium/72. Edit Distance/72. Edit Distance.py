# from: horse
# into: ros

# Init:
# horse
# ro s

# 1. horse -> rorse
# 2. rorse -> rose
# 3. rose -> ros


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        m, n = len(word1), len(word2)
        if not m or not n:
            return max(m, n)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

        return dp[m][n]


solution = Solution()
print(solution.minDistance(word1="horse", word2="ros"))  # 3
print(solution.minDistance(word1="intention", word2="execution"))  # 5
