package main

func moveZeroes(nums []int) {
	left := 0

	for right := 0; right < len(nums); right++ {
		if nums[right] != 0 {
			nums[right], nums[left] = nums[left], nums[right]
			left += 1
		}
	}
}
