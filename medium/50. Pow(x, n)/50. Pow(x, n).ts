function myPow(x: number, n: number): number {
    if (!n)
        return 1

    if (n < 0) {
        x = 1 / x
        n = Math.abs(n)
    }

    return x ** n
};