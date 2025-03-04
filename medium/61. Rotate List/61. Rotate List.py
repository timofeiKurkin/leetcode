from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 0
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        
        k %= length
        if not k:
            return head
        
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        tail = head
        
        return new_head

        # There is no way to solve this task by recursion
        # def run(curr: Optional[ListNode], i: int) -> Tuple[Optional[ListNode], int]:
        #     if not curr:
        #         return (curr, 0)
        #     if not curr.next:
        #         return (curr, ((i + k) % i))
        #     next_item, return_i = run(curr.next, i + 1)
        #     if return_i:
        #         next_item.next = curr
        #         return (next_item, return_i - 1)
        #     else:
        #         curr.next = next_item
        #         return (curr, 0)
        # res, _ = run(head, 0)
        # return res
        


# print((i + k) % i)
# print((3 + 2) % 3)
# print((3 + 4) % 3)
