package main

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findMin(node TreeNode) TreeNode {
	for node.Left != nil {
		node = *node.Left
	}

	return node
}

func updateNode(node *TreeNode) *TreeNode {
	if node.Left == nil {
		return node.Right
	}
	if node.Right == nil {
		return node.Left
	}

	minValue := findMin(*node.Right)
	node.Val = minValue.Val
	node.Right = deleteNode(node.Right, minValue.Val)
	return node
}

func run(node *TreeNode, key int) (bool, *TreeNode) {
	if node == nil {
		return false, nil
	}

	if node.Val == key {
		return true, updateNode(node)
	}

	status, right := run(node.Right, key)
	if status {
		node.Right = right
		return true, node
	} else {
		_, left := run(node.Left, key)
		node.Left = left
		return false, node
	}
}

func deleteNode(root *TreeNode, key int) *TreeNode {
	_, res := run(root, key)
	return res
}
