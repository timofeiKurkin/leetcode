function finalPrices(prices: number[]): number[] {
    const res: number[] = []

    for (let i = 0; i < prices.length; i++) {
        const price = prices[i]
        let discount = 0

        for (let j = i + 1; j < prices.length; j++) {
            if (prices[j] <= prices[i]) {
                discount = prices[j]
                break
            }
        }

        res.push(price - discount)
    }

    return res
};