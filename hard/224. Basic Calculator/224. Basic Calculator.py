from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        stack: List[int] = []
        result = 0
        prev_number = 0

        sign = 1

        def update_result() -> int:
            return result + sign * prev_number

        for element in s:
            if element.isdigit():
                prev_number = prev_number * 10 + int(element)

            elif element in "+-":
                result = update_result()
                prev_number = 0
                sign = 1 if element == "+" else -1

            elif element == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif element == ")":
                result = update_result()
                prev_number = 0
                result *= stack.pop()
                result += stack.pop()

        result = update_result()
        return result


solution = Solution()
print(solution.calculate(s="1 + 1"))  # 2
print(" ")
print(solution.calculate(s=" 2-1 + 2 "))  # 3
print(" ")
print(solution.calculate(s="(1+(4+5+2)-3)+(6+8)"))  # 23
print(" ")
print(solution.calculate(s="2147483647"))
print(" ")
print(solution.calculate(s="1-(     -2)"))  # 3
print(" ")
print(solution.calculate(s="-2+ 1"))  # -1
print(" ")
print(solution.calculate(s="- (3 + (4 + 5))"))  # -12
