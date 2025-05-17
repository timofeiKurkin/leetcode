package main

import "math"

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxLevelSum(root *TreeNode) int {
	i := 1
	level := i
	maxSum := math.MinInt

	queue := []*TreeNode{root}

	for len(queue) > 0 {
		levelSum := 0
		levelSize := len(queue)

		for j := 0; j < levelSize; j++ {
			node := queue[0]
			queue = queue[1:]

			levelSum += node.Val

			if node.Left != nil {
				queue = append(queue, node.Left)
			}

			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}

		if levelSum > maxSum {
			maxSum = levelSum
			level = i
		}

		i += 1
	}

	return level
}
