package main

import "math"

func findMaxAverage(nums []int, k int) float64 {
	n := len(nums)
	res := -math.Pow(10, 5)
	left := 0
	curr_sum := 0

	for i := 0; i < k-1; i++ {
		curr_sum += nums[i]
	}

	for right := k - 1; right < n; right++ {
		curr_sum += nums[right]
		res = max(res, float64(curr_sum)/float64(k))
		curr_sum -= nums[left]
		left += 1
	}

	return float64(res)
}
