function isHappy(n: number): boolean {
    // const seen = new Map()
    const seen: number[] = []

    while (n !== 1) {
        if (seen.find((i) => i === n))
            return false
        seen.push(n)

        let sum = 0
        for (const digit of n.toString()) {
            sum += Number(digit) ** 2
        }

        n = sum
    }

    return true
};

console.log(isHappy(19))