class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split()

        if len(pattern) != len(s_arr):
            return False

        pattern_to_word = {}
        word_to_pattern = {}

        for p, w in zip(pattern, s_arr):
            if pattern_to_word.get(p, w) != w or word_to_pattern.get(w, p) != p:
                return False
            pattern_to_word[p] = w
            word_to_pattern[w] = p

        return True
