function totalMoney(n: number): number {
    return solution2(n)
};

function solution1(n: number): number {
    function mod(a: number, b: number) {
        return a % b
    }

    function div(a: number, b: number) {
        return (a - a % b) / b
    }

    const weeks = div(n, 7), days = mod(n, 7)
    return 28 * weeks + 7 * Math.floor((weeks * (weeks - 1)) / 2) + Math.floor((2 * weeks + days + 1) * days / 2)
}

function solution2(n: number): number {
    // =======
    // =======
    // ====

    function arithmeticalSum(from: number, to: number) {
        // return (from + to) * Math.floor((to - from + 1) / 2)
        let sum = 0
        while (from <= to) {
            sum += from
            from += 1
        }
        return sum
    }

    if (n <= 7) {
        return arithmeticalSum(1, n)
    }

    const fullWeeks = Math.floor(n / 7)
    let startMoney = 1, res = 0

    while (startMoney <= fullWeeks) {
        res += arithmeticalSum(startMoney, startMoney + 6)
        startMoney += 1
    }

    if (n % 7 !== 0) {
        const remain = n - (7 * fullWeeks)
        res += arithmeticalSum(startMoney, startMoney + remain - 1)
    }

    return res
}