/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function detectCycle(head: ListNode | null): ListNode | null {
    if (!head) return null

    const ht = new Map()

    let first: ListNode | null = head
    while (first) {
        if (ht.has(first)) {
            ht.delete(first)
            break
        }

        ht.set(first, 1)
        first = first.next
    }

    let second: ListNode | null = head
    while (second) {
        if (!ht.delete(second)) return second
        second = second.next
    }

    return null
};