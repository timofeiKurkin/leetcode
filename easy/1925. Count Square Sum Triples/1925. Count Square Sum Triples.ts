function countTriples(n: number): number {
    return solution2(n)
};

function solution1(n: number): number {
    let res = 0

    for (let a = 1; a <= n; a++) {
        for (let b = a + 1; b <= n; b++) {
            const square = a ** 2 + b ** 2
            const c = Math.round(square ** 0.5)

            if (c <= n && c ** 2 === square)
                res += 2
        }
    }

    return res
}

function solution2(n: number): number {
    const gcd = (x: number, y: number): number => !y ? x : gcd(y, x % y)

    let res = 0

    for (let u = 2; u * u <= n; u++) {
        for (let v = 1; v < u; v++) {
            if (~(u - v) & 1 || gcd(u, v) !== 1) continue;
            const c = u * u + v * v
            if (c > n) continue
            res += Number(n / c) << 1
        }
    }

    return res
}