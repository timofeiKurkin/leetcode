from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_len = 0
        curr = head
        while curr:
            curr = curr.next
            list_len += 1

        curr = head

        new_list = ListNode(0)
        curr_new = new_list

        for _ in range(0, (list_len // k) * k, k):
            if not curr or not curr.next:
                break

            next_val: Optional[ListNode] = None

            step = 0
            while step < k and curr:
                next_val = ListNode(curr.val, next_val)
                curr = curr.next
                step += 1

            curr_new.next = next_val

            while curr_new.next:
                curr_new = curr_new.next

        if curr:
            curr_new.next = curr

        return new_list.next


solution = Solution()

ex1_5 = ListNode(5)
ex1_4 = ListNode(4, ex1_5)
ex1_3 = ListNode(3, ex1_4)
ex1_2 = ListNode(2, ex1_3)
ex1_1 = ListNode(1, ex1_2)

example_1 = ex1_1

res = solution.reverseKGroup(example_1, 2)

while res:
    print(res.val)
    res = res.next

# print(solution.reverseKGroup(example_2, 3))
