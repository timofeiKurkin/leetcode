// 92. Reverse Linked List II


class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

const node5 = new ListNode(5)
const node4 = new ListNode(4, node5)
const node3 = new ListNode(3, node4)
const node2 = new ListNode(2, node3)
const node1 = new ListNode(1, node2)

function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    if (!head || right === left) return head

    let first = new ListNode(0, head)
    // first.next = head
    let prev = first // position after which need to flip the list

    for (let i = 0; i < left - 1; i++) {
        prev = prev.next!
    }

    let curr = prev.next // left position in the list

    for(let i = 0; i < right - left; i++) {
        if(!curr || !curr.next) break // break if curr or curr.next is empty

        let next = curr.next // choose next item. left + 1
        curr.next = next.next // left + 1 = left + 1 + 1
        next.next = prev.next // left + 1 + 1 = left
        prev.next = next
    }

    return first.next

};

console.log(reverseBetween(node1, 2, 4));


export { }