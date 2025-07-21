class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) == 1:
            return s

        res = list(s)[:2]
        prev = res[-1]
        prev_two = res[-2]

        for sym in s[2:]:
            if prev == prev_two == sym:
                continue

            prev_two = prev
            prev = sym
            res.append(sym)

        return "".join(res)
