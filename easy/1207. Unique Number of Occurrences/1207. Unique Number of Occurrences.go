package main

func uniqueOccurrences(arr []int) bool {
	items := make(map[int]int)
	for _, n := range arr {
		items[n] += 1
	}

	occurs := make(map[int]bool)

	for k := range items {
		if occurs[items[k]] {
			return false
		}
		occurs[items[k]] = true
	}

	return true
}
