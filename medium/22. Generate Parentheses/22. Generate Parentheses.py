from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []
        o, c = "(", ")"

        def backtrack(path: str, opened: int, closed: int) -> None:
            if len(path) == n * 2:
                res.append(path)
                return

            if opened < n:
                backtrack(path + o, opened + 1, closed)

            if closed < opened:
                backtrack(path + c, opened, closed + 1)

            return

        backtrack("", 0, 0)
        return res


solution = Solution()
print(
    solution.generateParenthesis(n=3)
)  # ["((()))","(()())","(())()","()(())","()()()"]
# print(solution.generateParenthesis(n=1))  # ["()"]
# print(
#     solution.generateParenthesis(n=4)
# )  # ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
