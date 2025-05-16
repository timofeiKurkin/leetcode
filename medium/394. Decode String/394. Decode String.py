from typing import Tuple


class Solution:
    # def dfs(self, s: str) -> Tuple[str, int]:
    #     digit_end = 1

    #     while s[digit_end].isdigit():
    #         digit_end += 1

    #     k = int(s[0:digit_end])
    #     res = ""

    #     i = digit_end
    #     while i < len(s):
    #         v = s[i]

    #         if v == "[":
    #             i += 1
    #         elif v == "]":
    #             break
    #         elif v.isdigit():
    #             sub, end = self.dfs(s[i:])
    #             i += end
    #             res += sub
    #         else:
    #             res += v
    #             i += 1

    #     return res * k, i + 1

    def decodeString(self, s: str) -> str:
        # if len(s) == 1:
        #     return s

        # res = ""
        # i = 0

        # while i < len(s):
        #     value = s[i]

        #     if value.isdigit():
        #         sub, end = self.dfs(s[i:])
        #         res += sub
        #         i += end
        #     else:
        #         res += value
        #         i += 1

        # return res

        def dfs(i: int) -> Tuple[str, int]:
            res = ""

            while i < len(s):
                if s[i].isdigit():
                    k = 0

                    while s[i].isdigit():
                        k = k * 10 + int(s[i])
                        i += 1

                    i += 1
                    decoded_str, i = dfs(i)
                    res += decoded_str * k
                elif s[i] == "]":
                    return res, i + 1
                else:
                    res += s[i]
                    i += 1

            return res, i

        res, _ = dfs(0)
        return res


solution = Solution()
# print(solution.decodeString(s="3[a]2[bc]"))
# print(solution.decodeString(s="3[a2[c]]"))
# print(solution.decodeString(s="2[abc]3[cd]ef"))

# abcabc cdcdcd ef
# abcabc d] ef

# print("123[abc]"[0:])
print("1[abc]"[1])
