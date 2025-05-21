from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # n = 0
        # curr = head
        # while curr:
        #     n += 1
        #     curr = curr.next

        # odd = ListNode(0)
        # odd_p = odd
        # even = ListNode(0)
        # even_p = even
        # i = 1

        # while head:
        #     if i % 2 == 0:
        #         even_p.next = ListNode(head.val)
        #         even_p = even_p.next
        #     else:
        #         odd_p.next = ListNode(head.val)
        #         odd_p = odd_p.next

        #     i += 1
        #     head = head.next

        # odd_p.next = even.next

        # return odd.next

        if head == None or head.next == None or head.next.next == None:
            return head

        odd = head
        even_head: Optional[ListNode] = head.next
        even: Optional[ListNode] = even_head

        while even and even.next:
            odd.next = even.next
            odd: ListNode = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head
