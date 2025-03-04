from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_head = ListNode(0)  # Set a new head for linked list
        curr = new_head  # Set current as new_head. Due to this I can merge two lists

        while list1 and list2:  # While list one and two isn't empty
            if (
                list1.val <= list2.val
            ):  # If list one is less than list two, set curr.next
                curr.next = list1
                list1 = list1.next
            else:  # Otherwise set curr next list two
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2  # Set last head from one of them

        return new_head.next
