from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head and not head.next:
            return head

        new_head: ListNode = ListNode(0, head)  # Создать новую переменную со списком
        prev = new_head  # Переменная для перебора элементов в new_head списке
        curr = head  # Создать переменную для итерации по head

        # Написать цикл, в котором при обнаружении дубликатов запускать другой цикл для их удаления
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return new_head.next
