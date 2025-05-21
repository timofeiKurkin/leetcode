from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = deque()
        curr = head

        while curr:
            nums.append(curr.val)
            curr = curr.next

        mid = len(nums) // 2
        curr = head
        res = 0

        for _ in range(mid):
            if curr:
                res = max(res, curr.val + nums.popleft())
                curr = curr.next

        return res
