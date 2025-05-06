package main

import "slices"

func kidsWithCandies(candies []int, extraCandies int) []bool {
	n := len(candies)
	res := slices.Repeat([]bool{false}, n)
	max_candy := slices.Max(candies)

	for i, candy := range candies {
		res[i] = candy+extraCandies >= max_candy
	}

	return res
}
