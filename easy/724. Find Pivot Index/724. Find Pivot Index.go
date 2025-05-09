package main

func countSum(nums []int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	return sum
}

func pivotIndex(nums []int) int {
	total_sum := countSum(nums)
	n := len(nums)
	leftSum := 0

	for i := 0; i < n; i++ {
		rightSum := total_sum - nums[i] - leftSum
		if rightSum == leftSum {
			return i
		}
		leftSum += nums[i]
	}

	return -1
}
