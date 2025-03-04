/**
 * Definition for singly-linked list.
 */


class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}


function sortList(head: ListNode | null): ListNode | null {
    if (!head || !head.next)
        return head

    let slow: ListNode | null = head
    let fast: ListNode | null = head.next

    while (fast && fast.next) {
        slow = slow.next!
        fast = fast.next.next
    }

    const middle = slow.next
    slow.next = null

    const right = sortList(middle)
    const left = sortList(head)

    return merge(right, left)
};


function merge(firstPart: ListNode | null, secondPart: ListNode | null): ListNode | null {
    const newHead = new ListNode(0)
    let curr = newHead

    while (firstPart && secondPart) {
        if (firstPart.val < secondPart.val) {
            curr.next = firstPart
            firstPart = firstPart.next
        } else {
            curr.next = secondPart
            secondPart = secondPart.next
        }
        curr = curr.next
    }

    curr.next = firstPart || secondPart

    return newHead.next
}
