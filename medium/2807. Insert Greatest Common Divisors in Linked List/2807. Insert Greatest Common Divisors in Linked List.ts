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

function gcd(a: number, b: number): number {
    if (!b) {
        return a
    }
    return gcd(b, a % b)
}

function insertGreatestCommonDivisors(head: ListNode | null): ListNode | null {
    let curr = head

    while (curr?.next) {
        curr.next = new ListNode(gcd(curr.val, curr.next.val), curr.next)
        curr = curr.next.next
    }

    return head
};

export { }

