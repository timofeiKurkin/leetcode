class Solution:
    def reverseWords(self, s: str) -> str:
        # if len(s) == 1:
        #     return s
        # s = s.strip()
        # i = 0
        # while i < len(s):
        #     if s[i] == " " and s[i + 1] == " ":
        #         s = s[:i] + s[i + 1 :]
        #     else:
        #         i += 1
        # s_arr = s.split(" ")
        # s_arr.reverse()
        # return " ".join(s_arr)

        a = s.strip().split()
        return "".join(a[::-1])


solution = Solution()

s_1 = "the sky is blue"
s_2 = "  hello world  "
s_3 = "a good   example"

print(solution.reverseWords(s_1))
print(solution.reverseWords(s_2))
print(solution.reverseWords(s_3))
