function minimumOperations(nums: number[]): number {
    let res = 0

    for (const num of nums) {
        if (num % 3 !== 0) res += 1
        // res += Math.min(findDivisibleNumber(num, 3, 1), findDivisibleNumber(num, 3, -1))
    }

    return res
};

function findDivisibleNumber(num: number, divisor: number, direction: number): number {
    let steps = 0

    while (num % divisor !== 0) {
        num += direction
        steps += 1
    }

    return steps
}
