from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: Optional[ListNode], headB: Optional[ListNode]
    ) -> Optional[ListNode]:
        first, second = headA, headB
        ht = {}

        while first:
            ht[first] = True
            first = first.next

        while second:
            if ht[second]:
                return second
            second = second.next

        return None
