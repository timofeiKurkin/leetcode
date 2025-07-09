from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr_head: Optional[ListNode] = head

        new_head = ListNode(0)
        curr = new_head

        while curr_head and curr_head.next:
            first = curr_head.next.next
            second = curr_head.next

            second.next = curr_head
            curr_head.next = first
            curr.next = second

            curr = curr_head
            curr_head = first

        return new_head.next
