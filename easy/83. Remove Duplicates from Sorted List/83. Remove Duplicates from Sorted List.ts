// 83. Remove Duplicates from Sorted List
// Дано: отсортированный связанный список целочисленных элементов, где элементы могут повторяться.
// Условие: вернуть список, не содержащий повторы



class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

const node5 = new ListNode(3)
const node4 = new ListNode(1, node5)
const node3 = new ListNode(1, node4)
const node2 = new ListNode(1, node3)
const node1 = new ListNode(1, node2)

function deleteDuplicates(head: ListNode | null): ListNode | null {
    if (!head) return head

    let first = new ListNode(0, head)
    let prev: ListNode | null = first.next

    while (prev && prev.next) {
        if (prev.val === prev.next.val) prev.next = prev.next.next
        else prev = prev.next
    }

    return first.next
};

console.log(deleteDuplicates(node1));

export { }