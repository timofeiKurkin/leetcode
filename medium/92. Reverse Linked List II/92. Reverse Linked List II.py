# 92. Reverse Linked List II
# Дано: односвязный список элементов, а также значения left и right, между которыми нужно перевернуть порядок элементов
# Условие: вернуть связанный список с перевернутым порядком элементов в некоторых позициях.

# Пример 1:
# Вход: head = [1,2,3,4,5], left = 2, right = 4
# Выход: [1,4,3,2,5]

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node_7 = ListNode(7, None)
node_6 = ListNode(6, node_7)
node_5 = ListNode(5, node_6)
node_4 = ListNode(4, node_5)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # last_elements: ListNode | None = head
        # last_index = 1
        # while last_elements:
        #     if last_index <= right:
        #         last_elements = last_elements.next
        #         last_index += 1
        #     else:
        #         break

        # first: ListNode | None = ListNode(head.val)  # First element of the lined list
        # prev: ListNode | None = (
        #     None  # Reversed list with elements that have starting on the left and ending on the right
        # )
        # curr: ListNode = head  # Just current element during while cycle
        # index = 1  # For controlling position between left and right

        # while curr:
        #     next: ListNode | None = curr.next
        #     if index >= left and index <= right:
        #         curr.next = prev or last_elements
        #         prev = curr
        #         curr = next
        #         index += 1
        #     else:
        #         if left == 1:
        #             first = prev
        #         else:
        #             first.next = prev
        #         break

        #     # if not first:
        #     #     curr.next = None
        #     #     first = curr
        #     #     curr = next
        #     #     index += 1
        #     # else:
        #     #     if index <= right and index >= left:
        #     #         curr.next = prev or last_elements
        #     #         prev = curr
        #     #         curr = next
        #     #         index += 1
        #     #     elif index > right:
        #     #         if not first.next:
        #     #             first.next = prev
        #     #         break

        if not head or left == right:
            return head

        first = ListNode(0)
        first.next = head
        prev = first

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next
        next_val = None

        for _ in range(right - left):
            if not curr or not curr.next:
                break

            next_val = curr.next  # link on the next item
            curr.next = next_val.next or None
            next_val.next = prev.next
            prev.next = next_val

        return first.next


solution = Solution()

items = []
res = solution.reverseBetween(node_1, 2, 4)
while res:
    items.append(res.val)
    res = res.next
print(items)
