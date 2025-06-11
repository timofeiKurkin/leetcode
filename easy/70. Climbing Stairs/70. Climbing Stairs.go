package main

import "slices"

func climbStairs(n int) int {
	// TLE
	// 	if n < 0 {
	// 		return 0
	// 	}
	//     if n == 0 {
	//         return 1
	//     }
	// 	return climbStairs(n-1) + climbStairs(n-2)

	dp := slices.Repeat([]int{1}, n+1)
	dp[0] = 1 // top
	dp[1] = 1 // 1 + 1 = top

	for i := 2; i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}

	return dp[len(dp)-1]
}
