// 82. Remove Duplicates from Sorted List II
// Дано: отсортированный связанный список целочисленных элементов, где элементы могут повторяться.
// Условие: вернуть список, который не содержит повторяющиеся числа из исходного списка


class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

const node7 = new ListNode(5)
const node6 = new ListNode(4, node7)
const node5 = new ListNode(4, node6)
const node4 = new ListNode(3, node5)
const node3 = new ListNode(3, node4)
const node2 = new ListNode(2, node3)
const node1 = new ListNode(1, node2)

function deleteDuplicates(head: ListNode | null): ListNode | null {
    // if (!head) return head
    // if (head && !head.next) return head

    // let first = new ListNode(0, head)
    // let prev: ListNode | null = first
    // let curr: ListNode | null = first.next
    // const test = new Map()

    // while (curr && curr.next) {
    //     if (curr.val === curr.next.val) {
    //         test.set(curr.val, curr.val)
    //         curr.next = curr.next.next
    //     } else curr = curr.next
    // }

    // while (prev && prev.next) {
    //     if (test.has(prev.next.val)) {
    //         prev.next = prev.next.next
    //     } else prev = prev.next
    // }

    // return first.next

    if (!head) return head
    if (head && !head.next) return head

    let first = new ListNode(0, head)
    let prev: ListNode | null = first
    let curr: ListNode | null = head

    while(prev && curr) {
        if(curr.next && curr.val === curr.next.val) {
            while(curr.next && curr.val === curr.next.val) {
                curr = curr.next
            }
            prev.next = curr.next
        } else {
            prev = prev.next
        }
        curr = curr.next
    }

    return first.next
};

const res = deleteDuplicates(node1)

const resArr: number[] = []
let step = res
while (step) {
    resArr.push(step.val)
    step = step.next
}
console.log(resArr);

export { }