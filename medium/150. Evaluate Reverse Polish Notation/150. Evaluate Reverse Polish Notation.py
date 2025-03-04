from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return 1

        stack: List[int] = []

        for element in tokens:
            if element not in "/*-+":
                stack.append(int(element))
            else:
                right = stack.pop()
                left = stack.pop()

                if element == "/":
                    stack.append(int(left / right))
                if element == "*":
                    stack.append(left * right)
                if element == "+":
                    stack.append(left + right)
                if element == "-":
                    stack.append(left - right)

        return stack.pop()


solution = Solution()
print(solution.evalRPN(tokens=["2", "1", "+", "3", "*"]))
print(solution.evalRPN(tokens=["4", "13", "5", "/", "+"]))
print(
    solution.evalRPN(
        tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)

print(int(1.5))
print(int(1.386523232))
print(int(534.53323232))
