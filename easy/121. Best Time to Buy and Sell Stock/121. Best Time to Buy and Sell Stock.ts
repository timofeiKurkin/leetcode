// 121. Best Time to Buy and Sell Stock
// Дано: массив цен prices, где каждый элемент prices[i] - это цена акции в i день.
// Условие: получить максимальную выгоду с покупки акции. Купить по меньшей цене в определенный день и продать по большей цене в следующий из дней. Нельзя купить сегодня, а продать завтра. Нужно вернуть максимальный профит с покупки и продажи. Например, если купил за 1 и продал за 6, значит профит - 5.


// Example 1:
// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

// Example 2:
// Input: prices = [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transactions are done and the max profit = 0.

const prices1 = [7, 1, 5, 3, 6, 4]
const prices2 = [7, 6, 4, 3, 1]
const prices3 = [3, 3]
const prices4 = [2, 4, 1]
const prices5 = [3, 2, 6, 5, 0, 3]

function maxProfit(prices: number[]): number {
    // const max = Math.max(...prices.slice(prices.indexOf(min), -1))
    // return prices.indexOf(max)

    // const min = Math.min(...prices) // Нужно линейное решение. Дни идут поочередно
    // let bestPrice = 0
    // for(let i = prices.indexOf(min); i <= prices.length; i++) {
    //     if (bestPrice < prices[i]) bestPrice = prices[i]
    // }
    // return bestPrice - min

    let buy = [0, prices[0]], profit = 0
    for (let i = 0; i <= prices.length; i++) {
        if (prices[i] < buy[1]) {
            buy = [i, prices[i]]
        } else {
            const newProfit = prices[i] - buy[1]
            if (newProfit > profit) profit = newProfit
        }
    }

    return profit
};

console.log(maxProfit(prices1)); // 5
console.log(maxProfit(prices2)); // 0
console.log(maxProfit(prices3)); // 0
console.log(maxProfit(prices4)); // 2
console.log(maxProfit(prices5)); // 4

export { }