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

func dfs(root *TreeNode, maxNode int) int {
	if root == nil {
		return 0
	}

	isGood := 0
	if maxNode <= root.Val {
		isGood = 1
	}
	maxNode = max(maxNode, root.Val)

	return isGood + dfs(root.Left, maxNode) + dfs(root.Right, maxNode)
}

func goodNodes(root *TreeNode) int {
	return dfs(root, math.MinInt)
}
