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

func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}

	middle := int(math.Round(float64(len(nums) / 2)))
	left := sortedArrayToBST(nums[middle:])
	right := sortedArrayToBST(nums[middle+1:])
	return &TreeNode{Val: nums[middle], Left: left, Right: right}
}
