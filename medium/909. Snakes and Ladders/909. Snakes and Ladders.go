package main

import (
	"math"
	"slices"
)

func getIntoPosition(square, n int) (int, int) {
	row := (square - 1) / n
	column := (square - 1) % n
	if row%2 == 1 {
		column = n - 1 - column
	}

	return row, column
}

func snakesAndLadders(board [][]int) int {
	n := len(board)
	target := math.Pow(float64(n), 2)
	slices.Reverse(board)

	queue := [][]int{{1, 0}}
	visited := make(map[int]bool)

	for len(queue) > 0 {
		item := queue[len(queue)-1]
		square, steps := item[0], item[1]
		queue = queue[1:]

		for i := 1; i < 7; i++ {
			nextSquare := square + i
			row, column := getIntoPosition(nextSquare, n)

			if board[row][column] != -1 {
				nextSquare = board[row][column]
			}
			if nextSquare == int(target) {
				return steps + 1
			}
			if visited[nextSquare] == false {
				visited[nextSquare] = true
				queue = append(queue, []int{nextSquare, steps + 1})
			}
		}
	}

	return -1
}
