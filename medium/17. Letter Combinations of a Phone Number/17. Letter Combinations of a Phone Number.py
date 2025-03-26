from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []

        phone_keyboard = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtrack(index: int, combination: str) -> None:
            if index == len(digits):
                res.append(combination)
                return

            digit = digits[index]
            for letter in phone_keyboard[digit]:
                backtrack(index + 1, combination + letter)

        backtrack(0, "")
        return list(res)


solution = Solution()

print(solution.letterCombinations("23"))
print(solution.letterCombinations(""))
print(solution.letterCombinations("2"))
print(solution.letterCombinations("79"))
print(
    solution.letterCombinations("22")
)  # ["aa","ab","ac","ba","bb","bc","ca","cb","cc"]
#    ['aa','ab','ac',    ,'bb','bc',    ,    ,'cc']
#    ['aa','ab','ac','ba','bb','bc','ca','cb','cc'] - with duplicates
