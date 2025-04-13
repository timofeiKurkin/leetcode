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

const reverse = (start: ListNode | null, k: number): [(ListNode | null), (ListNode | null)] => {
    let prev: ListNode | null = null, curr = start
    while (k && curr) {
        const nxt: ListNode | null = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        k -= 1
    }

    return [prev, curr]
}

function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    let length = 0
    let curr = head
    while (curr) {
        length += 1
        curr = curr.next
    }

    const dummy = new ListNode(0)
    dummy.next = head
    let groupTail: ListNode | null = dummy
    curr = head

    while (length >= k) {
        const tail = curr
        const [reversedHead, nextGroupTail] = reverse(curr, k)

        if (groupTail)
            groupTail.next = reversedHead

        if (tail)
            tail.next = nextGroupTail

        groupTail = tail
        curr = nextGroupTail
        length -= k
    }

    return dummy.next
};

export { }

