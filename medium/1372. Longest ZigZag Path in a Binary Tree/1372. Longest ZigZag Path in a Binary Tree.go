package main

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Direction int

const (
	Right Direction = 1
	Left  Direction = -1
)

func dfs(root *TreeNode, dir Direction, sum int) int {
	if root == nil {
		return sum
	}

	if root.Left == nil && root.Right == nil {
		return sum + 1
	}

	if dir == Right {
		return max(dfs(root.Left, Left, sum+1), dfs(root.Right, Right, 0))
	} else {
		return max(dfs(root.Right, Right, sum+1), dfs(root.Left, Left, 0))
	}
}

func longestZigZag(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return max(dfs(root.Left, Left, 0), dfs(root.Right, Right, 0))
}
