class Solution:
    def reverseVowels(self, s: str) -> str:
        v_set = {'a', 'e', 'i', 'o', 'u'}
        v_arr = []

        s = list(s)

        for sym in s:
            if sym.lower() in v_set:
                v_arr.append(sym)
        
        for i in range(len(s)):
            if s[i].lower() in v_set:
                s[i] = v_arr.pop()

        return "".join(s)