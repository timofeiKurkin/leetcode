function isPerfectSquare(num: number): boolean {
    // return (Math.sqrt(num)) % 1 === 0

    if (num < 2) return true

    let left = 2, right = Math.floor(num / 2)

    while (left <= right) {
        const middle = Math.floor((left + right) / 2)
        const square = middle * middle

        if (square === num) {
            return true
        } else if (square < num) {
            left = middle + 1
        } else {
            right = middle - 1
        }
    }

    return false
};