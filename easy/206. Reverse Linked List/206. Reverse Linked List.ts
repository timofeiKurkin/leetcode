// 206. Reverse Linked List
// Дано: односвязный список элементов
// Условие: перевернуть порядок элементов и вернуть новый массив. Если массив пустой, то вернуть его

// Пример 1:
// Вход: head = [1,2,3,4,5]
// Выход: [5,4,3,2,1]

// Пример 2:
// Вход: head = [1,2]
// Выход: [2,1]

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
const node1 = new ListNode(1, node2)

function reverseList(head: ListNode | null): ListNode | null {
    if (!head) return null

    let prev = null
    let current: ListNode | null = head

    while (current) {
        let next: ListNode | null = current.next
        current.next = prev
        prev = current
        current = next
    }

    return prev
};

const res = reverseList(node1)
console.log(res);


// const resArr = []
// let step = res
// while(step && step?.next) {
//     resArr.push(step.val)
//     step = step.next
//     if (!step) break
// }
// console.log(resArr);

export { }
