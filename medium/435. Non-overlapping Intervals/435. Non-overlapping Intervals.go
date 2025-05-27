package main

import "sort"

func eraseOverlapIntervals(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1]
	})

	deleted := 0
	prev := intervals[0][1]

	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] < prev {
			deleted += 1
		} else {
			prev = intervals[i][1]
		}
	}

	return deleted
}
