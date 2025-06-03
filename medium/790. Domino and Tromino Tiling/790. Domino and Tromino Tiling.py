class Solution:
    def numTilings(self, n: int) -> int:
        return sol2(n)


def sol1(n: int) -> int:
    F, T, B = {0: 1, 1: 1}, {1: 0}, {1: 0}

    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2] + T[i - 1] + B[i - 1]
        T[i] = B[i - 1] + F[i - 2]
        B[i] = F[i - 2] + T[i - 1]

    return F[n] % (10**9 + 7)


def sol2(n: int) -> int:
    FF, F, T, B = 1, 1, 0, 0

    for i in range(2, n + 1):
        FF, F, T, B = F, F + FF + B + T, B + FF, T + FF

    return F % (10**9 + 7)
