package main

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {
	var run func(root *TreeNode) []int
	run = func(root *TreeNode) []int {
		if root == nil {
			return []int{}
		}

		return append(append(run(root.Left), root.Val), run(root.Right)...)
	}

	return run(root)[k-1]
}
