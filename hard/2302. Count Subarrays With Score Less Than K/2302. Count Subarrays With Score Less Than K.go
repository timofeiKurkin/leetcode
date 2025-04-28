package main

func countSubarrays(nums []int, k int64) int64 {
	res := 0
	left := 0
	curr_sum := 0

	for right := 0; right < len(nums); right++ {
		curr_sum += nums[right]

		for int64(curr_sum*(right-left+1)) >= k {
			curr_sum -= nums[left]
			left += 1
		}

		res += max(0, right-left+1)
	}

	return int64(res)
}
