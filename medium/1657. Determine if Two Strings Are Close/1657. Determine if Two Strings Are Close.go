package main

import "sort"

func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}

	d1 := make(map[rune]int)
	d2 := make(map[rune]int)

	for i := 0; i < len(word1); i++ {
		d1[rune(word1[i])] += 1
		d2[rune(word2[i])] += 1
	}

	a1 := []int{}
	a2 := []int{}

	for d := range d1 {
		if _, v := d2[d]; !v {
			return false
		}

		a1 = append(a1, d1[d])
	}

	for d := range d2 {
		if _, v := d1[d]; !v {
			return false
		}

		a2 = append(a2, d2[d])
	}

	sort.Ints(a1)
	sort.Ints(a2)

	for i := 0; i < len(a1); i++ {
		if a1[i] != a2[i] {
			return false
		}
	}

	return true
}
