class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 1 or not s:
        #     return len(s)
        # n = len(s)
        # max_length = 0
        # for left in range(n):
        #     symbol = s[left]
        #     window_str = symbol
        #     for right in range(left + 1, n):
        #         if s[right] in window_str:
        #             break
        #         window_str += s[right]
        #     max_length = max(max_length, len(window_str))
        # return max_length

        left = 0
        max_length = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            max_length = max(max_length, (right - left) + 1)
            seen.add(s[right])

        return max_length


solution = Solution()
print(solution.lengthOfLongestSubstring(s="abcabcbb"))
print(solution.lengthOfLongestSubstring(s="bbbbb"))
print(solution.lengthOfLongestSubstring(s="pwwkew"))
print(solution.lengthOfLongestSubstring(s="au"))
