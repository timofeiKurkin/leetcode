# Find: the longest palindromic substring in s

# Example 1:
# Input: babad
# Output: bab


# Example 2:
# Input: skdolodf
# Output: dolod


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # # dp: List[int] = [1] * len(s)
        # max_substr = ""

        # for end in range(len(s)):
        #     start = 0

        #     while start <= end:
        #         substr = s[start : end + 1]
        #         substr_reversed = "".join(list(substr)[::-1])

        #         if substr == substr_reversed:
        #             # dp[end] = end - start
        #             max_substr = substr if len(substr) > len(max_substr) else max_substr
        #             break

        #         start += 1

        # # max_length = max(dp)
        # # index = dp.index(max_length)
        # # return s[index - max_length : (index - max_length) + max_length]
        # return max_substr

        n = len(s)

        if n == 1:
            return s

        def palindrome_from_center(start: int, end: int) -> str:
            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1 : end]

        max_substr = ""

        for i in range(n):
            even_substr = palindrome_from_center(i, i)
            odd_substr = palindrome_from_center(i, i + 1)

            max_substr = max(even_substr, odd_substr, max_substr, key=len)

        return max_substr


solution = Solution()
print(solution.longestPalindrome(s="babad"))
print(solution.longestPalindrome(s="cbbd"))
print(solution.longestPalindrome(s="skdolodf"))
print(solution.longestPalindrome(s="a"))
print(solution.longestPalindrome(s="aa"))
print(solution.longestPalindrome(s="aaa"))
print(solution.longestPalindrome(s="aaaa"))
print(solution.longestPalindrome(s="aaaab"))
