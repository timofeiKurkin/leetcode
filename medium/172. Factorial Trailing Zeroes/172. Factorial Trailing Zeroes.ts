function trailingZeroes(n: number): number {
    let zeroes = 0
    let i = 5

    while (i <= n) {
        zeroes += Math.floor(n / i)
        i *= 5
    }

    return zeroes
};

console.log(trailingZeroes(3))
console.log(trailingZeroes(5))
console.log(trailingZeroes(0))
console.log(trailingZeroes(7))
console.log(trailingZeroes(1574))