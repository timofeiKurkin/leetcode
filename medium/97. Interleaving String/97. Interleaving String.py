# Interleaving string formula:
#


class Solution:
    # def findLetters(
    #     self, root_s: str, part_s: Deque[str], positions: List[int]
    # ) -> None:
    #     for i, s in enumerate(root_s):
    #         if not part_s:
    #             break

    #         if part_s[0] == s and positions[i] != 0:
    #             positions[i] = 0
    #             part_s.popleft()

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # positions = [-1] * len(s3)
        # if s1:
        #     self.findLetters(s3, deque(s1), positions)
        # if s2:
        #     self.findLetters(s3, deque(s2), positions)

        # return -1 not in positions

        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = ((dp[i - 1][j]) and s1[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return dp[m][n]


solution = Solution()
print(solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
# aadbbcbcac
# --d-b-b-ac - s1
# --d-b-b-ac - s2

print(solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
# aadbbbaccc
# --d-bba--c - s1
# --d-bba--c - s2

print(solution.isInterleave(s1="", s2="", s3=""))
print(solution.isInterleave(s1="a", s2="", s3="a"))
print(solution.isInterleave(s1="aabc", s2="abad", s3="aabcabad"))
# aabcabad
# ----abad - s1
# aabcabad - s2
