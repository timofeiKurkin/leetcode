package main

import "slices"

func countSubarrays(nums []int, k int) int64 {
	max_v := slices.Max(nums)

	res := 0
	left := 0
	k_count := 0

	for right := 0; right < len(nums); right++ {
		if nums[right] == max_v {
			k_count += 1
		}

		for k_count > k {
			if nums[left] == k {
				k_count -= 1
			}
			left += 1
		}

		res += left
	}
	
	return int64(res)
}
