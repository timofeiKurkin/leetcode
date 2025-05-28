package main

import "slices"

func dailyTemperatures(temperatures []int) []int {
	n := len(temperatures)
	res := slices.Repeat([]int{0}, n)
	stack := []int{}

	for i := 0; i < n; i++ {
		for len(stack) > 0 && temperatures[i] > temperatures[stack[len(stack)-1]] {
			prev := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			res[prev] = i - prev
		}

		stack = append(stack, i)
	}

	return res
}
