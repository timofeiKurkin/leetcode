package main

func longestSubarray(nums []int) int {
	if len(nums) == 1 {
		return 0
	}

	left := 0
	res := 0
	remind := 1

	for right := 0; right < len(nums); right++ {
		if nums[right] == 0 {
			if remind == 1 {
				remind = 0
			} else {
				for remind == 0 {
					if nums[left] == 0 {
						remind = 1
					}
					left += 1
				}
				remind = 0
			}
		}

		res = max(res, right-left)
	}

	return res
}
