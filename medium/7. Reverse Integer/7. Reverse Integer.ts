function reverse(x: number): number {
    const dir = x >= 0 ? 1 : -1
    let res = 0
    x = Math.abs(x)

    while (x) {
        const remain = Math.abs(x % 10)
        res *= 10
        res += remain

        x -= remain
        x /= 10
    }

    return res > 0x7FFFFFFF ? 0 : res * dir
};