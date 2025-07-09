// 21. Merge Two Sorted Lists
// Дано: два отсортированных связанных списка. Каждое значение списка может повторяться
// Условие: вернуть объединенный связанный список из двух списков с сохранением последовательности (сортировки от меньшего к большему)

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

const node6 = new ListNode(4)
const node5 = new ListNode(3, node6)
const node4 = new ListNode(1, node5)

const node3 = new ListNode(4)
const node2 = new ListNode(2, node3)
const node1 = new ListNode(1, node2)

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    // if (!list1 && !list2) return null
    // if (!list1 && list2) return list2
    // if (!list2 && list1) return list1

    let newHead = new ListNode(0)
    let curr = newHead // New linked list

    while (list1 && list2) { // While list1 and list 2 aren't empty
        if (list1.val <= list2.val) { // Algorithm: sorting by the lowest value
            curr.next = list1
            list1 = list1.next
        } else {
            curr.next = list2
            list2 = list2.next
        }
        curr = curr.next
    }

    curr.next = list1 || list2 // Set remains

    return newHead.next
};

const res = mergeTwoLists(node1, node4);

const resArr: number[] = []
let step = res
while (step) {
    resArr.push(step.val)
    step = step.next
}
console.log(resArr);

export {}