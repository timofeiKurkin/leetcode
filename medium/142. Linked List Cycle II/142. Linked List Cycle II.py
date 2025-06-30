from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.solution2(head)

    def solution1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        ht = {}

        first = head
        while first:
            if first in ht:
                del ht[first]
                first = first.next
                break

            ht[first] = True
            first = first.next

        second = head
        while second:
            if second not in ht:
                return second

            second = second.next

        return None

    def solution2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow: ListNode = head
        fast: Optional[ListNode] = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next

        return slow
