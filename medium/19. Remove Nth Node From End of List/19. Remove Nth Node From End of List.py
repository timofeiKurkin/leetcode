from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # list_for_counting = head
        # list_length = 0
        # while list_for_counting:
        #     list_length += 1
        #     list_for_counting = list_for_counting.next

        # removing_index = list_length - n
        # new_head = ListNode("data", next=head)
        # curr = new_head

        # while curr and curr.next and removing_index:
        #     removing_index -= 1
        #     curr = curr.next

        # if not removing_index and curr and curr.next and curr.next.next:
        #     curr.next = curr.next.next
        # else:
        #     curr.next = None

        # return new_head.next
        
        dummy = ListNode(0, head)
        first = second = dummy
        
        for _ in range(n + 1):
            first = first.next
            
        while first:
            first, second = first.next, second.next
        
        second.next = second.next.next
        
        return dummy.next
