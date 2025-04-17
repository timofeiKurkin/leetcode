package main

import "fmt"

func maxProfit(prices []int) int {
	n := len(prices)
	if n == 0 {
		return n
	}

	purchases := 2
	dp := make([][]int, purchases+1)
	for i := range dp {
		dp[i] = make([]int, n)
	}

	for purchase := 1; purchase <= purchases; purchase++ {
		minPrice := prices[0]

		for i := 1; i < n; i++ {
			minPrice = min(minPrice, prices[i]-dp[purchase-1][i-1])
			dp[purchase][i] = max(dp[purchase][i-1], prices[i]-minPrice)
		}
	}

	return dp[2][n-1]
}

func main() {
	fmt.Print(maxProfit([]int{3, 3, 5, 0, 0, 3, 1, 4}))
	fmt.Print(maxProfit([]int{1, 2, 3, 4, 5}))
	fmt.Print(maxProfit([]int{7, 6, 4, 3, 1}))
}
