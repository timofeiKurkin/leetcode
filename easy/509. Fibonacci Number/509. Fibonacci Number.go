package main

import (
	"fmt"
	"slices"
)

func fib(n int) int {
	if n == 0 {
		return 0
	}

	dp := slices.Repeat([]int{0}, n+1)
	dp[1] = 1

	for i := 2; i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}
	fmt.Println(dp)

	return dp[n]
}
