class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isPalindrome(left - 1, right) or isPalindrome(left, right + 1)
            left += 1
            right -= 1

        return True
