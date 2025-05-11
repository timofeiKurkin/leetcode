package main

import (
	"fmt"
	"strings"
)

func equalPairs(grid [][]int) int {
	row := make(map[string]int)
	n := len(grid)

	for r := 0; r < n; r++ {
		key := encode(grid[r])
		row[key] += 1
	}

	res := 0

	for c := 0; c < n; c++ {
		col := make([]int, n)

		for r := 0; r < n; r++ {
			col[r] = grid[r][c]
		}

		key := encode(col)
		res += row[key]
	}

	return res
}

func encode(arr []int) string {
	sb := strings.Builder{}
	for _, num := range arr {
		sb.WriteString(fmt.Sprintf("%d,", num))
	}
	return sb.String()
}
