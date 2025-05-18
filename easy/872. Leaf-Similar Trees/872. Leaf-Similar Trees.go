package main

import (
	"reflect"
)

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(root *TreeNode, leafList *[]int) {
	if root != nil {
		if root.Left == nil && root.Right == nil {
			*leafList = append(*leafList, root.Val)
		}
		dfs(root.Left, leafList)
		dfs(root.Right, leafList)
	}
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	list1 := make([]int, 0)
	list2 := make([]int, 0)

	dfs(root1, &list1)
	dfs(root2, &list2)

	return reflect.DeepEqual(list1, list2)
}
