class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # First not working solution. Problem test -> s="badc", t="baba"
        # unique_s = ""
        # for i in range(len(s) - 1):
        #     if s[i] != s[i + 1]:
        #         unique_s += s[i]
        # unique_t = ""
        # for i in range(len(t) - 1):
        #     if t[i] != t[i + 1]:
        #         unique_t += t[i]
        # return len(unique_s) == len(unique_t)

        # Second not working solution. Problem test -> s="badc", t="baba"
        # for i in range(len(s) - 1):
        #     if (s[i] == s[i + 1] and t[i] != t[i + 1]) or (
        #         s[i] != s[i + 1] and t[i] == t[i + 1]
        #     ):
        #         return False

        # return True

        map_s_to_t = {}
        map_t_to_s = {}

        for i in range(len(s)):
            if s[i] not in map_s_to_t:
                map_s_to_t[s[i]] = t[i]

            if t[i] not in map_t_to_s:
                map_t_to_s[t[i]] = s[i]

            if map_s_to_t[s[i]] != t[i]:
                return False

            if map_t_to_s[t[i]] != s[i]:
                return False

        return True


solution = Solution()

print(solution.isIsomorphic(s="egg", t="add"))
print(solution.isIsomorphic(s="foo", t="bar"))
print(solution.isIsomorphic(s="paper", t="title"))
print(solution.isIsomorphic(s="bbbaaaba", t="aaabbbba"))
print(solution.isIsomorphic(s="badc", t="baba"))
