package main

import (
	"sort"
)

func findMinArrowShots(points [][]int) int {
	sort.Slice(points, func(i, j int) bool {
		return points[i][len(points[i])-1] < points[j][len(points[j])-1]
	})

	arrows := 1
	end := points[0][1]

	for i := 1; i < len(points); i++ {
		if points[i][0] > end {
			arrows += 1
			end = points[i][1]
		}
	}

	return arrows
}

func main() {
	findMinArrowShots([][]int{{10, 16}, {2, 8}, {1, 6}, {7, 12}})
}
