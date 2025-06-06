package main

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	if root.Val == p.Val || root.Val == q.Val {
		return root
	}

	left := lowestCommonAncestor(root.Right, p, q)
	right := lowestCommonAncestor(root.Left, p, q)

	if left != nil && right != nil {
		return root
	} else if left != nil {
        return left
    } else {
        return right
    }
}
