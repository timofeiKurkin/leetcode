function arrSum(nums: number[]) {
    let sum = 0
    for (const num of nums) {
        sum += num
    }
    return sum
}

function peopleAwareOfSecret(n: number, delay: number, forget: number): number {
    const MOD = 10 ** 9 + 7
    let dp = new Array<number>(forget).fill(0)
    dp[0] = 1

    for (let i = 0; i < n - 1; i++) {
        dp = [0, ...dp.slice(0, -1)]
        dp[0] = arrSum(dp.slice(delay,)) % MOD
    }

    return arrSum(dp) % MOD
};

console.log(peopleAwareOfSecret(6, 2, 4))
console.log(peopleAwareOfSecret(4, 1, 3))
