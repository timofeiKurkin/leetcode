package main

func triangularSum(nums []int) int {
	n := len(nums)

	for n > 0 {
		for i := 0; i < n-1; i++ {
			nums[i] = (nums[i] + nums[i+1]) % 10
		}
		n -= 1
	}

	return nums[0]
}
