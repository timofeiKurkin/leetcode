class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        return self.solution2(s, x, y)

    def solution1(self, s: str, x: int, y: int) -> int:
        res = 0

        while "ab" in s or "ba" in s:
            prev = len(s)

            if y > x:
                while "ba" in s:
                    s = s.replace("ba", "")

                    res += ((prev - len(s)) // 2) * y
                    prev = len(s)

                while "ab" in s:
                    s = s.replace("ab", "")

                    res += ((prev - len(s)) // 2) * x
                    prev = len(s)

            else:
                while "ab" in s:
                    s = s.replace("ab", "")

                    res += ((prev - len(s)) // 2) * x
                    prev = len(s)

                while "ba" in s:
                    s = s.replace("ba", "")

                    res += ((prev - len(s)) // 2) * y
                    prev = len(s)

        return res

    def solution2(self, s: str, x: int, y: int) -> int:
        res = 0
        ch1, ch2 = "a", "b"
        cnt1, cnt2 = 0, 0

        if x < y:
            x, y = y, x
            ch1, ch2 = "b", "a"

        for ch in s:
            if ch == ch1:
                cnt1 += 1
            elif ch == ch2:
                if cnt1 > 0:
                    cnt1 -= 1
                    res += x
                else:
                    cnt2 += 1
            else:
                res += min(cnt1, cnt2) * y
                cnt1 = cnt2 = 0

        if cnt1 != 0:
            res += min(cnt1, cnt2) * y

        return res
