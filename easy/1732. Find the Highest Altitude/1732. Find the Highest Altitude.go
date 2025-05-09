package main

import "slices"

func largestAltitude(gain []int) int {
	n := len(gain)
	altitudes := slices.Repeat([]int{0}, n+1)

	for i := 0; i < n; i++ {
		altitudes[i+1] = altitudes[i] + gain[i]
	}

	return slices.Max(altitudes)
}
