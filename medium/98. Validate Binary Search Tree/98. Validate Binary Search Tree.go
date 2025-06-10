package main

import (
	"slices"
)

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func run(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	return slices.Concat(run(root.Left), []int{root.Val}, run(root.Right))
}

func isValidBST(root *TreeNode) bool {
	nodes := run(root)

	for i := 1; i < len(nodes); i++ {
		if nodes[i-1] >= nodes[i] {
			return false
		}
	}

	return true
}
