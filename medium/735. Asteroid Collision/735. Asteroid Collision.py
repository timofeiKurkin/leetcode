from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = []

        # while asteroids:
        #     asteroid = asteroids.pop(0)

        #     if asteroid < 0:
        #         while len(stack) and stack[-1] > 0:
        #             if stack[-1] + asteroid == 0:
        #                 asteroid = 0
        #                 stack.pop()
        #                 break
        #             elif stack[-1] + asteroid > 0:
        #                 asteroid = 0
        #                 break
        #             else:
        #                 stack.pop()

        #         if asteroid != 0:
        #             stack.append(asteroid)
        #     else:
        #         stack.append(asteroid)

        # return stack

        stack = []
        for ast in asteroids:
            if not stack or ast > 0:
                stack.append(ast)
            else:
                while stack and ast != 0 and stack[-1] > 0:
                    if stack[-1] + ast < 0:
                        stack.pop()
                    elif stack[-1] + ast == 0:
                        stack.pop()
                        ast = 0
                        break
                    elif stack[-1] + ast > 0:
                        ast = 0
                        break

                if (not stack or stack[-1] < 0) and ast:
                    stack.append(ast)

        return stack


solution = Solution()
print(solution.asteroidCollision(asteroids=[5, 10, -5]))
print(solution.asteroidCollision(asteroids=[8, -8]))
print(solution.asteroidCollision(asteroids=[10, 2, -5]))
print(solution.asteroidCollision(asteroids=[5, 12, -30, 7, 9, 23, -10]))
print(solution.asteroidCollision(asteroids=[1, -2, 10, -5]))
print(solution.asteroidCollision(asteroids=[-4, 6]))
print(solution.asteroidCollision(asteroids=[4, -6]))
