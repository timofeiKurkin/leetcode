from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        prev: ListNode | None = None
        slow: ListNode = head
        fast: ListNode | None = head

        while fast and fast.next:
            fast = fast.next.next

            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        if fast:
            slow = slow.next

        while slow and prev:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next

        return True
