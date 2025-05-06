package main

import "slices"

func buildArray(nums []int) []int {
	ans := slices.Repeat([]int{0}, len(nums))

	for i := 0; i < len(nums); i++ {
		ans[i] = nums[nums[i]]
	}

	return ans
}
