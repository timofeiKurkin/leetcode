function arrangeCoins(n: number): number {
    let res = 0
    let low = 0, high = 2 ** 32

    while (low <= high) {
        const middle = low + Math.floor((high - low) / 2)

        if (isValidLevel(middle, n)) {
            res = middle
            low = middle + 1
        } else {
            high = middle - 1
        }
    }

    return res
};

function isValidLevel(value: number, total: number): boolean {
    return Math.floor(value * (value + 1) / 2) <= total
}