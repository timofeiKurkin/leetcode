function numSquares(n: number): number {
    const dp = new Array<number>(n + 1).fill(n)
    dp[0] = 0

    for (let target = 1; target <= n; target++) {
        for (let i = 1; i <= target; i++) {
            const square = i ** 2
            if (square > target) break
            dp[target] = Math.min(dp[target], (dp[target - square] || 0) + 1)
        }
    }

    return dp[n]
};
