from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # words_set = set(words)
        # freq_root = defaultdict(int)

        # for word in words:
        #     freq_root[word] += 1

        # n = len(words[0])
        # right, left = 0, 0

        # freq_sub = defaultdict(int)
        # start = -1

        # indices: List[int] = []

        # while right <= len(s):
        #     substring = s[left:right]

        #     if len(substring) >= n:
        #         word = substring[-n:]

        #         if word in words_set:
        #             if start == -1:
        #                 start = left

        #             if word in freq_sub and freq_sub[word] == freq_root[word]:
        #                 freq_sub.clear()
        #                 left += n
        #                 right = left + 1
        #                 start = -1
        #             else:
        #                 freq_sub[word] += 1

        #             if len(freq_sub) == len(words_set):
        #                 allowed = True
        #                 for key in words_set:
        #                     if freq_sub[key] != freq_root[key]:
        #                         allowed = False
        #                         break

        #                 if allowed:
        #                     indices.append(start)
        #                     start = -1
        #                     left += n
        #                     right = left
        #                     freq_sub.clear()
        #                 else:
        #                     right += n
        #             else:
        #                 right += n

        #         else:
        #             freq_sub.clear()
        #             left = right
        #             right += 1
        #             start = -1

        #     else:
        #         right += 1

        # return indices

        n, m = len(words), len(words[0])
        window_size = m * n
        word_count = Counter(words)
        indices = []

        for i in range(m):
            left = i
            right = i
            curr_count = Counter()

            while right + m <= len(s):
                word = s[right : right + m]
                right += m

                if word in word_count:
                    curr_count[word] += 1

                    while curr_count[word] > word_count[word]:
                        left_word = s[left : left + m]
                        curr_count[left_word] -= 1
                        left += m

                    if right - left == window_size:
                        indices.append(left)
                else:
                    curr_count.clear()
                    left = right

        return indices


solution = Solution()
print(solution.findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))  # [0, 9]
print(
    solution.findSubstring(
        s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]
    )
)  # []
print(
    solution.findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"])
)  # [6, 9, 12]
print(
    solution.findSubstring(s="barkakabumfoothefoobarman", words=["foo", "bar"])
)  # [16]
