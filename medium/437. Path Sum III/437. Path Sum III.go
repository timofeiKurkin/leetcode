package main

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// func findPaths(node *TreeNode, curr_sum int) int {
// 	if node == nil {
// 		return 0
// 	}

// 	curr_sum += node.Val
// 	match := 0
// 	if curr_sum == tar

// 	return 0
// }

func pathSum(root *TreeNode, targetSum int) int {
	if root == nil {
		return 0
	}

	var findPaths func(node *TreeNode, curr_sum int) int

	findPaths = func(node *TreeNode, curr_sum int) int {
		if node == nil {
			return 0
		}

		curr_sum += node.Val
		match := 0

		if curr_sum == targetSum {
			match = 1
		}

		return match + findPaths(node.Left, curr_sum) + findPaths(node.Right, curr_sum)
	}

	return findPaths(root, 0) + pathSum(root.Left, targetSum) + pathSum(root.Right, targetSum)
}
