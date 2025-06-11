package main

import "slices"

func rob(nums []int) int {
	n := len(nums)
	// prev1 := 0
	// prev2 := nums[0]
	dp := slices.Repeat([]int{0}, n)
	dp[0] = nums[0]
	dp[1] = max(nums[0], nums[1])

	for i := 2; i < n; i++ {
		// max_rob := max(prev2, prev1+nums[i])
		// prev1 = prev2
		// prev2 = max_rob
		dp[i] = max(dp[i-1], dp[i-2]+nums[i])
	}

	// return prev2
	return dp[n-1]
}
