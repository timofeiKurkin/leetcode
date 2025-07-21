from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.solution1(head, n)

    def solution1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = end = dummy

        for _ in range(n + 1):
            if start:
                start = start.next

        while start:
            start, end = start.next, end.next

        if end:
            end.next = end.next.next if end.next else None

        return dummy.next
