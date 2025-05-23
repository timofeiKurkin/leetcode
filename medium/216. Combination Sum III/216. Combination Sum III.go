package main

import "slices"

func combinationSum3(k int, n int) [][]int {
	if k > n {
		return [][]int{}
	}

	res := [][]int{}

	var backtrack func(items []int, curr_sum int, combination []int)
	backtrack = func(items []int, curr_sum int, combination []int) {
		if curr_sum > n || len(combination) > k || (curr_sum == n && len(combination) < k) {
			return
		}

		if curr_sum == n {
			res = append(res, combination)
			return
		}

		for _, item := range items {
			if !slices.Contains(combination, item) {
				backtrack(items[1:], curr_sum+item, slices.Concat(combination, []int{item}))
			} else {
				return
			}
		}
	}

	backtrack([]int{1, 2, 3, 4, 5, 6, 7, 8, 9}, 0, []int{})

	return res
}
