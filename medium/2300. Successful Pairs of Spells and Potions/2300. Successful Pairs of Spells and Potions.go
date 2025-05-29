package main

import (
	"slices"
)

func successfulPairs(spells []int, potions []int, success int64) []int {
	n := len(potions)
	slices.Sort(potions)
	p := []int{}

	for _, s := range spells {
		biggest := potions[n-1] * s

		if biggest < int(success) {
			p = append(p, 0)
			continue
		}

		left, right := 0, n-1
		for left < right {
			mid := (right + left) / 2
			if potions[mid]*s < int(success) {
				left = mid + 1
			} else {
				right = mid
			}
		}

		p = append(p, n-left)
	}

	return p
}
