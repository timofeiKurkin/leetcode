package main

import "math"

func increasingTriplet(nums []int) bool {
	firstItem := math.MaxInt32
	secondItem := math.MaxInt32

	for _, num := range nums {
		if num <= firstItem {
			firstItem = num
		} else if num <= secondItem {
			secondItem = num
		} else {
			return true
		}
	}

	return false
}
