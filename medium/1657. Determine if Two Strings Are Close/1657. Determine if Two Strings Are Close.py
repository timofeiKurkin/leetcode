from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        # if set(word1) != set(word2):
        #     return False

        # w1_dict = defaultdict(int)
        # for w in word1:
        #     w1_dict[w] += 1

        # w2_dict = defaultdict(int)
        # for w in word2:
        #     w2_dict[w] += 1

        # w1_count = [i for _, i in w1_dict.items()]
        # w2_count = [i for _, i in w2_dict.items()]

        # w1_count.sort()
        # w2_count.sort()

        # for i in range(len(w1_count)):
        #     if w1_count[i] != w2_count[i]:
        #         return False

        # return True

        d1 = Counter(word1)
        d2 = Counter(word2)

        if set(d1.keys()) != set(d2.keys()):
            return False

        return sorted(d1.values()) == sorted(d2.values())
