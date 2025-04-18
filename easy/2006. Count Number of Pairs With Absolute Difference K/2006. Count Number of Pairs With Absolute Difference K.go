package main

func absDiffInt(x, y int) int {
	if x < y {
		return y - x
	}
	return x - y
}

func countKDifference(nums []int, k int) int {
	res := 0
	n := len(nums)

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if absDiffInt(nums[i], nums[j]) == k {
				res += 1
			}
		}
	}

	return res
}
