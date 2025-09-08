function kthFactor(n: number, k: number): number {
    return solution2(n, k)
};

function solution1(n: number, k: number): number {
    const items: number[] = []

    for (let i = 1; i <= n; i++) {
        const num = n / i
        if (num % 1 == 0) {
            items.push(num)
        }
    }

    return items.length >= k ? items[items.length - k] : -1
}

function solution2(n: number, k: number): number {
    let step = 0

    for (let factor = 1; factor <= n; factor++) {
        if (n / factor % 1 == 0) {
            step += 1
            if (step === k) return factor
        }
    }

    return -1
}

export { }

