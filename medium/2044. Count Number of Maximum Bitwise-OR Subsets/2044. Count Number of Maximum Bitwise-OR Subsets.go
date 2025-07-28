package main

import "fmt"

func countMaxOrSubsets(nums []int) int {
	maxBitwiseOr := 0
	res := 0

	for _, num := range nums {
		maxBitwiseOr |= num
	}

	fmt.Println(maxBitwiseOr)

	var backtrack func(index, orValue int)

	backtrack = func(index, orValue int) {
		if orValue == maxBitwiseOr {
			res += 1
		}

		for i := index; i < len(nums); i++ {
			backtrack(index+1, orValue|nums[i])
		}
	}

	backtrack(0, 0)

	return res
}
