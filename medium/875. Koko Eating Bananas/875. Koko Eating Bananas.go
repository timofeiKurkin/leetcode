package main

import (
	"slices"
)

func canEatAllBananas(mid, h int, piles []int) bool {
	hours := 0

	for _, pile := range piles {
		hours += (pile + mid - 1) / mid
	}

	return hours <= h
}

func minEatingSpeed(piles []int, h int) int {
	left, right := 1, slices.Max(piles)

	for left < right {
		mid := left + (right-left)/2

		if canEatAllBananas(mid, h, piles) {
			right = mid
		} else {
			left = mid + 1
		}
	}

	return left
}
