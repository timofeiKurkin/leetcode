function maxProfit(prices: number[]): number {
    const n = prices.length
    if (!n) return n

    const maxPurchases = 2
    const dp: number[][] = Array.from({ length: maxPurchases + 1 }, () => new Array(n).fill(0))

    for (let purchase = 1; purchase <= maxPurchases; purchase++) {
        let minPrice = prices[0]

        for (let i = 1; i <= n; i++) {
            minPrice = Math.min(minPrice, prices[i] - dp[purchase - 1][i - 1])
            dp[purchase][i] = Math.max(dp[purchase][i - 1], prices[i] - minPrice)
        }
    }

    return dp[2][n - 1]
};

console.log(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
console.log(maxProfit([1, 2, 3, 4, 5]))
console.log(maxProfit([7, 6, 4, 3, 1]))

export { }

