package main

import (
	"fmt"
	"slices"
)

func sortColors(nums []int) {
	count := make([]int, 0, slices.Max(nums)+1)
	fmt.Println(count)
	for _, num := range nums {
		count[num] += 1
	}

	i := 0
	for num := 0; num < len(count); num++ {
		for j := 0; j < count[num]; j++ {
			nums[i] = num
			i += 1
		}
	}
}
