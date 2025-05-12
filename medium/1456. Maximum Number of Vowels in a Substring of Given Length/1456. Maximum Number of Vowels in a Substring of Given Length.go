package main

import (
	"slices"
)

func maxVowels(s string, k int) int {
	vowels := []byte{'a', 'e', 'i', 'o', 'u'}
	count := 0
	res := -1

	for i := 0; i < k-1; i++ {
		if slices.ContainsFunc(vowels, func(v byte) bool {
			return s[i] == v
		}) {
			count += 1
		}
	}

	n := len(s)
	left := 0

	for right := k - 1; right < n; right++ {
		if slices.ContainsFunc(vowels, func(v byte) bool {
			return s[right] == v
		}) {
			count += 1
		}

		res = max(res, count)

		if slices.ContainsFunc(vowels, func(v byte) bool {
			return s[left] == v
		}) {
			count -= 1
		}

		left += 1
	}

	return res
}
