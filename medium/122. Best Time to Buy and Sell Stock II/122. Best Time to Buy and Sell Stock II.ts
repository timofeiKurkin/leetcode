function maxProfit(prices: number[]): number {
    let profit = 0

    for (let i = 0; i < prices.length; i++) {
        const newProfit = prices[i + 1] - prices[i]
        if (newProfit > 0) {
            profit += newProfit
        }
    }

    return profit
};