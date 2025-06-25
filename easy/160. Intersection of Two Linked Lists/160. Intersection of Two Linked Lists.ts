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

function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    let first = headA, second = headB
    const ht = new Map()

    while (first) {
        ht.set(first, true)
        first = first.next
    }

    while (second) {
        if (ht.has(second)) return second
        second = second.next
    }

    return null
};

export { }

