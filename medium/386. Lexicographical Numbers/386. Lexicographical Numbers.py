from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # Easy way
        # return sorted(range(1, n + 1), key=str)

        # Iterative way
        res = []
        curr = 1

        for _ in range(n):
            res.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                if curr >= n:
                    curr //= 10
                curr += 1
                while curr % 10 == 0:
                    curr //= 10

        return res


solution = Solution()
print(solution.lexicalOrder(5 * (10**4)))
