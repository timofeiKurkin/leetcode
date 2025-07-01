class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 0
        # cnt = Counter(word)
        # for _, count in cnt.items():
        #     res += count - 1
        # return res + 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                res += 1

        return res
