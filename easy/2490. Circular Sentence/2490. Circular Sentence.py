class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence_arr = sentence.split(" ")

        if len(sentence) == 1:
            word = sentence_arr[0]
            return word[0] == word[-1]

        for index in range(0, len(sentence_arr) - 1):
            current = sentence_arr[index]
            next = sentence_arr[index + 1]

            if current[-1] != next[0]:
                return False

        return sentence_arr[0][0] == sentence_arr[-1][-1]


solution = Solution()
print(solution.isCircularSentence("leetcode exercises sound delightful"))  # True
print(solution.isCircularSentence("eetcode"))  # True
print(solution.isCircularSentence("Leetcode is cool"))  # False
