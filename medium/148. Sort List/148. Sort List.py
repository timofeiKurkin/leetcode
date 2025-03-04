from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Determine the middle of the linked list
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(
        self, first_part: Optional[ListNode], second_part: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_head = ListNode(0)
        curr = new_head

        while first_part and second_part:
            if first_part.val < second_part.val:
                curr.next = first_part
                first_part = first_part.next
            else:
                curr.next = second_part
                second_part = second_part.next
            curr = curr.next

        curr.next = first_part or second_part

        return new_head.next
