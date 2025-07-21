from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return self.solution1(l1, l2)

    def solution1(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def getNumbers(l: Optional[ListNode], counter: str) -> str:
            if not l:
                return counter

            return getNumbers(l.next, str(l.val) + counter)

        first = int(getNumbers(l1, ""))
        second = int(getNumbers(l2, ""))

        (*list_sum,) = str(first + second)
        list_sum.reverse()

        head = ListNode(0)
        new_list = head

        for item in list_sum:
            new_list.next = ListNode(int(item))
            new_list = new_list.next

        return head.next

    def solution2(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            digit_l1 = l1.val if l1 else 0
            digit_l2 = l2.val if l2 else 0

            total = digit_l1 + digit_l2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next


solution = Solution()
print(
    solution.addTwoNumbers(
        ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))
    )
)
