from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # shortest_w = min(strs, key=len)
        # start = len(shortest_w)
        # for _ in range(start):
        #     status = True
        #     for word in strs:
        #         if shortest_w[:start] not in word:
        #             status = False
        #     if status:
        #         return shortest_w[:start]
        #     else:
        #         start -= 1
        # return ""

        if not strs:
            return ""

        prefix = strs[0]

        for world in strs[:1]:
            while not world.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
print(solution.longestCommonPrefix(["reflower", "flow", "flight"]))
