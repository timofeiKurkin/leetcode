package main

func maxProfit(k int, prices []int) int {
	n := len(prices)
	if n == 0 {
		return 0
	}

	profitActions := k
	dp := make([][]int, profitActions+1)

	for i := range dp {
		dp[i] = make([]int, n)
	}

	for action := 1; action <= profitActions; action++ {
		minPrice := prices[0]

		for i := 1; i < n; i++ {
			minPrice = min(minPrice, prices[i]-dp[action-1][i-1])
			dp[action][i] = max(dp[action][i-1], prices[i]-minPrice)
		}
	}

	return dp[profitActions][n-1]
}
