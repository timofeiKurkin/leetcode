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

function swapPairs(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return head

    let zero = new ListNode(0, head)

    let first: ListNode | null = head
    let newHead = head.next

    while (first && first.next) {
        const second = first.next
        const three = second.next

        second.next = first
        first.next = three
        zero.next = second

        zero = first
        first = zero.next
    }

    return newHead
};

export {}