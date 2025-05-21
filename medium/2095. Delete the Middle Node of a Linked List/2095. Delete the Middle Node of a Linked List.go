package main

/**
 * Definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteMiddle(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return nil
	}

	if head.Next.Next == nil {
		head.Next = nil
		return head
	}

	slow := head
	fast := head.Next.Next

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	slow.Next = slow.Next.Next
	return head
}
