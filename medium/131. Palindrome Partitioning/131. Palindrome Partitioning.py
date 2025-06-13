from typing import List


class Solution:
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res: List[List[str]] = []

        def backtrack(path: List[str], index: int):
            if index == n:
                res.append(path[:])
                return

            for i in range(index + 1, n + 1):
                if self.is_palindrome(s[index:i]):
                    backtrack(path + [s[index:i]], i)

        backtrack([], 0)

        return res
