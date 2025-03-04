class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        needle_length = len(needle)

        while index < len(haystack):
            right = index + needle_length

            if haystack[index:right] == needle:
                return index
            index += needle_length

        return -1


solution = Solution()

print(solution.strStr("sadbutsad", "sad"))
print(solution.strStr("leetcode", "leeto"))
