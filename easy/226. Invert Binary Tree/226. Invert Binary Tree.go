package main

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	if root.Left != nil || root.Right != nil {
		root = &TreeNode{Val: root.Val, Right: root.Right, Left: root.Left}
	}

	root = &TreeNode{Val: root.Val, Left: invertTree(root.Left), Right: invertTree(root.Right)}
	return root
}
