// 876. Middle of the Linked List


class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

const node5 = new ListNode(5)
const node4 = new ListNode(4, node5)
const node3 = new ListNode(3, node4)
const node2 = new ListNode(2, node3)
const node1 = new ListNode(2, node2)

// const node6 = new ListNode(6)
// const node5 = new ListNode(5, node6)
// const node4 = new ListNode(4, node5)
// const node3 = new ListNode(3, node4)
// const node2 = new ListNode(2, node3)
// const node1 = new ListNode(2, node2)

function middleNode(head: ListNode | null): ListNode | null {
    if (!head) return null

    let slow = head
    let fast = head

    while (fast && fast.next) {
        slow = slow.next!
        fast = fast.next.next!
        if (!fast) return slow
    }

    return slow
};


console.log(middleNode(node1));


export { }