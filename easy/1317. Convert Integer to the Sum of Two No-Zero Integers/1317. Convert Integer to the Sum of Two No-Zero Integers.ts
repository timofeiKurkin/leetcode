function getNoZeroIntegers(n: number): number[] {
    return solution2(n)
};

function solution1(n: number): number[] {
    let a = 1
    let b = n - 1

    while (b.toString().includes("0") || a.toString().includes("0")) {
        b -= 1
        a += 1
    }

    return [a, b]
}

function solution2(n: number): number[] {
    function noZero(num: number): boolean {
        while (num > 0) {
            if (num % 10 === 0) return false
            num /= 10
        }

        return true
    }

    for (let a = 1; a < n; a++) {
        let b = n - a
        if (noZero(a) && noZero(b)) return [a, b]
    }

    return []
}