package main

func longestOnes(nums []int, k int) int {
	count := 0
	res := 0
	left := 0
	remind := k

	for right := 0; right < len(nums); right++ {
		if nums[right] == 0 {
			count += 1
		} else {
			if remind != 0 {
				remind -= 1
				count += 1
			} else {
				for remind == 0 {
					if nums[left] == 0 {
						remind = 1
					}
					left += 1
					count -= 1
				}

				remind -= 1
				count += 1
			}
		}

		res = max(res, count)
	}

	return res
}
