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

function modifiedList(nums: number[], head: ListNode | null): ListNode | null {
    const set = new Set(nums)
    const newHead = new ListNode(0, head)
    let curr: ListNode | null = newHead

    while (curr && curr.next) {
        if (set.has(curr.next.val)) {
            curr.next = curr.next.next
        } else {
            curr = curr.next
        }
    }

    if (curr && set.has(curr.val)) {
        curr = null
    }

    return newHead.next
};

export { }

