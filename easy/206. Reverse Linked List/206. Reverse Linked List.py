from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev: ListNode | None = None
        curr: ListNode | None = head

        while curr:
            next: ListNode | None = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
