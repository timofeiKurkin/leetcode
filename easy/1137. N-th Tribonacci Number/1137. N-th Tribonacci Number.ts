function tribonacci(n: number): number {
    if (!n)
        return 0

    const dp = new Array<number>(n + 1).fill(0)
    dp[1] = dp[2] = 1

    for (let i = 3; i < dp.length; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    }

    return dp[dp.length - 1]
};

console.log(tribonacci(4))
console.log(tribonacci(25))