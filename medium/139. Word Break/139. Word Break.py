from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


solution = Solution()

print(solution.wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(solution.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(solution.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
print(solution.wordBreak(s="aaaaaaa", wordDict=["aaaa", "aaa"]))
print(solution.wordBreak(s="a", wordDict=["b"]))
