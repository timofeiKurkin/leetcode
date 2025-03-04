# (){}[]
# ({[]})
# ({()[]{}})
# ({[]})({[]})
# ({}()]
# ({()})


class Solution:
    def isValid(self, s: str) -> bool:
        # parentheses_open = {"(": ")", "{": "}", "[": "]"}
        if len(s) % 2 != 0:
            return False

        parentheses_open = set({"(", "{", "["})
        parentheses_close = {")": "(", "}": "{", "]": "["}

        stack = []

        for i in range(len(s)):
            # left: int = i + 1

            if s[i] in parentheses_open:  # Проверка, что скобка открывающаяся
                stack.append(s[i])

            elif s[i] in parentheses_close:
                if not stack or parentheses_close[s[i]] != stack.pop():
                    return False

            # while left < len(s):
            #     if len(stack) and s[left] in parentheses_close:
            #         if stack[-1] == parentheses_close[s[left]]:
            #             stack.pop()
            #             break
            #         # else:
            #         #     continue

            #     left += 1

        return not bool(stack)


solution = Solution()

print(solution.isValid("()"))  # True
print(solution.isValid("()[]{}"))  # True
print(solution.isValid("(]"))  # False
print(solution.isValid("([])"))  # True
print(solution.isValid("([)]"))
