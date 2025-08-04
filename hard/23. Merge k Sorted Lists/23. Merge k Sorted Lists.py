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
            return

        return self.solution2(lists)

    def solution1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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

    def solution2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes: list[ListNode] = []

        for node in lists:
            while node:
                nodes.append(node)
                node = node.next

        nodes.sort(key=lambda x: x.val)

        new_list = nodes[0] if nodes else None

        if new_list:
            for i, node in enumerate(nodes):
                node.next = nodes[i + 1] if i + 1 < len(nodes) else None

        return new_list
