package main

import "slices"

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 || len(inorder) == 0 {
		return nil
	}

	head := preorder[0]

	headIndex := slices.Index(inorder, head)
	if headIndex == -1 {
		return nil
	}

	left := buildTree(preorder[1:1+headIndex], inorder[:headIndex])
	right := buildTree(preorder[1+headIndex:], inorder[headIndex+1:])

	return &TreeNode{Val: head, Left: left, Right: right}
}
