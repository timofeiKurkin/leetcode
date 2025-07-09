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

function rotateRight(head: ListNode | null, k: number): ListNode | null {
    if (!head || !head.next || !k)
        return head

    let length = 1
    let tail = head
    while (tail?.next) {
        tail = tail.next
        length += 1
    }

    k %= length
    if (!k)
        return head

    let new_tail = head
    for (let i = 0; i < (length - k) - 1; i++) {
        if (new_tail.next)
            new_tail = new_tail.next
    }

    let new_head = new_tail.next
    new_tail.next = null
    tail.next = head

    return new_head
};


export { }
