package main

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func run(p, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}

	if p == nil || q == nil {
		return false
	}

	if p.Val != q.Val {
		return false
	}

	return run(p.Left, q.Right) && run(p.Right, q.Left)
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}

	return run(root.Left, root.Right)
}
