function maxProfit(k: number, prices: number[]): number {
    const n = prices.length
    if (!n)
        return 0

    const profitActions = k
    const dp: number[][] = Array.from({ length: profitActions + 1 }, () => new Array(n).fill(0))

    for (let action = 1; action <= profitActions; action++) {
        let minPrice = prices[0]

        for (let i = 1; i < n; i++) {
            minPrice = Math.min(minPrice, prices[i] - dp[action - 1][i - 1])
            dp[action][i] = Math.max(dp[action][i - 1], prices[i] - minPrice)
        }
    }

    return dp[profitActions][n - 1]
};

export { }

