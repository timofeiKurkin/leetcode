package main

func rob(nums []int) int {
	n := len(nums)
	prev1 := 0
	prev2 := nums[0]

	for i := 1; i < n; i++ {
		max_rob := max(prev2, prev1+nums[i])
		prev1 = prev2
		prev2 = max_rob
	}

	return prev2
}
