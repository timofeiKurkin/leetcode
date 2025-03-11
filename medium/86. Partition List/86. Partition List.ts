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

function partition(head: ListNode | null, x: number): ListNode | null {
    const low = new ListNode(0)
    let lowTail = low

    const great = new ListNode(0)
    let greatTail = great

    while (head) {
        if (head.val < x) {
            lowTail.next = new ListNode(head.val)
            lowTail = lowTail.next
        } else {
            greatTail.next = new ListNode(head.val)
            greatTail = greatTail.next
        }

        head = head.next
    }

    lowTail.next = great.next
    greatTail.next = null

    return low.next
};

export { }

