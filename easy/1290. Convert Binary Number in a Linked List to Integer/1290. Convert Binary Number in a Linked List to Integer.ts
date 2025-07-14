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


function getDecimalValue(head: ListNode | null): number {
    let res = 0
    while (head) {
        res += (res << 1) + head.val
        head = head.next
    }

    return res
};

export { }
