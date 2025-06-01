function minCostClimbingStairs(cost: number[]): number {
    const n = cost.length
    const dp = new Array<number>(n).fill(0)
    dp[n - 1] = cost[n - 1]
    dp[n - 2] = cost[n - 2]

    for (let i = n - 3; i >= 0; i--) {
        dp[i] = cost[i] + Math.min(dp[i + 1], dp[i + 2])
    }

    return Math.min(dp[0], dp[1])
};