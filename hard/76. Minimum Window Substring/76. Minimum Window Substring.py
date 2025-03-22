from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        have = {}
        required = len(need)
        formed = 0

        left, right = 0, 0
        min_window = ""

        while right < len(s):
            char = s[right]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            while left <= right and formed == required:
                if not min_window:
                    min_window = s[left : right + 1]
                elif len(s[left : right + 1]) < len(min_window):
                    min_window = s[left : right + 1]

                left_char = s[left]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1

                left += 1

            right += 1

        return min_window


solution = Solution()

print(solution.minWindow(s="ADOBECODEBANC", t="ABC"))
print(solution.minWindow(s="bba", t="ab"))
