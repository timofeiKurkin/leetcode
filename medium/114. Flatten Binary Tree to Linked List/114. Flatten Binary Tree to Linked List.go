package main

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func flatten(root *TreeNode) {
	if root == nil {
		return
	}

	flatten(root.Left)
	flatten(root.Right)

	rightSubtree := root.Right

	root.Right = root.Left
	root.Left = nil

	curr := root
	for curr.Right != nil {
		curr = curr.Right
	}

	curr.Right = rightSubtree
}
