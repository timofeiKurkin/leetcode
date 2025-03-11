from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lowest_nodes = ListNode(0)
        go_lowest_nodes = lowest_nodes

        greatest_nodes = ListNode(0)
        go_greatest_nodes = greatest_nodes

        while head:
            val = ListNode(head.val)
            if head.val < x:
                go_lowest_nodes.next = val
                go_lowest_nodes = go_lowest_nodes.next
            else:
                go_greatest_nodes.next = val
                go_greatest_nodes = go_greatest_nodes.next

            head = head.next

        go_lowest_nodes.next = greatest_nodes.next
        return lowest_nodes.next
