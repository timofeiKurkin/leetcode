class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s or not t:
            return True

        s_index = 0

        for symbol in t:
            if s[s_index] == symbol:
                s_index += 1

        return len(s) == s_index


solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))
print(solution.isSubsequence("axc", "ahbgdc"))
