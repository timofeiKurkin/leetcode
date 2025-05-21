from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        if not head.next.next:
            head.next = None
            return head

        prev: ListNode = ListNode(0)
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head

        while slow and fast and fast.next:
            prev.next = slow
            prev = prev.next
            slow = slow.next
            fast = fast.next.next

        assert slow is not None
        prev.next = slow.next
        return head
