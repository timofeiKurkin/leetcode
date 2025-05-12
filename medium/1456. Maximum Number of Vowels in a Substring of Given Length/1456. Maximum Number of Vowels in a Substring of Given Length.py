class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {"a", "e", "i", "o", "u"}
        count = 0
        res = -1

        for i in range(k - 1):
            if s[i] in vowels:
                count += 1

        left = 0
        for right in range(k - 1, n):
            if s[right] in vowels:
                count += 1

            res = max(res, count)

            if s[left] in vowels:
                count -= 1

            left += 1

        return res
