romanNums = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, roman: str) -> int:
        result = 0

        for i, s in enumerate(roman):
            currentNum = romanNums[s]

            if i + 1 <= len(roman) - 1:
                nextNum = romanNums[roman[i + 1]]
                if currentNum >= nextNum:
                    result += currentNum
                else:
                    result -= currentNum
            else:
                result += currentNum

        return result


solution = Solution()
print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))
