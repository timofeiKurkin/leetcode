class Solution:
    def removeStars(self, s: str) -> str:
        # res = ""

        # for i in range(len(s)):
        #     if s[i] == "*":
        #         res = res[:-1]
        #     else:
        #         res += s[i]

        # return res

        res = []
        for v in s:
            if v != "*":
                res.append(v)
            else:
                res.pop()
        return "".join(res)


solution = Solution()
print(solution.removeStars(s="leet**cod*e"))
print(solution.removeStars(s="erase*****"))
