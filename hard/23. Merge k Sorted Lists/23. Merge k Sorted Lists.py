import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        pq = []

        for i in range(len(lists)):
            linked_list = lists[i]

            while linked_list:
                heapq.heappush(pq, linked_list.val)
                linked_list = linked_list.next

        new_list = ListNode(0)
        curr = new_list

        while pq:
            item = heapq.heappop(pq)
            curr.next = ListNode(item)
            curr = curr.next

        return new_list.next
