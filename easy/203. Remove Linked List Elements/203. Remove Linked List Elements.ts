// 203. Remove Linked List Elements
// Дано: связанный список чисел. Они могут быть по порядку или нет - это не имеет значение. Также дан некий val, который является фильтрующим значением.
// Условие: удалить все элементы, где head.val === val и вернуть обновленный список.


class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

const node6 = new ListNode(4)
const node5 = new ListNode(6, node6)
const node4 = new ListNode(3, node5)
const node3 = new ListNode(6, node4)
const node2 = new ListNode(2, node3)
const node1 = new ListNode(1, node2)

function removeElements(head: ListNode | null, val: number): ListNode | null {
    if (!head) return null
    if (head && !head.next && head.val !== val) return head

    // let newHead: ListNode | null = new ListNode(head?.val)
    // let copy: ListNode | null = newHead
    // let curr: ListNode | null = head.next
    // while(curr) {
    //     if(curr.val !== val) {
    //         copy.next = new ListNode(curr.val)
    //         copy = copy.next
    //     }
    //     curr = curr.next
    // }
    // return newHead.val === val ? newHead.next : newHead

    let first = new ListNode(0, head)
    let curr = first

    while (curr.next) {
        if (curr.next.val === val) {
            curr.next = curr.next.next
        } else curr = curr.next
    }

    return first.next
};

console.log(removeElements(node1, 2));

export { }