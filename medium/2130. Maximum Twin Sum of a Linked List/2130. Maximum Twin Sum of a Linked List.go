package main

/**
 * Definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func pairSum(head *ListNode) int {
	// nums := []int{}
	// curr := head
	// for curr != nil {
	// 	nums = append(nums, curr.Val)
	// 	curr = curr.Next
	// }

	// mid := len(nums) / 2
	// curr = head
	// res := 0

	// for mid != 0 {
	// 	res = max(res, curr.Val+nums[len(nums)])
	// 	nums = nums[:len(nums)-1]
	// 	curr = curr.Next
	// 	mid -= 1
	// }

	// return res

	slow := head
	fast := head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	var prev *ListNode
	curr := slow
	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}

	res := 0

	for prev != nil {
		res = max(res, prev.Val+head.Val)
		head = head.Next
		prev = prev.Next
	}

	return res
}
