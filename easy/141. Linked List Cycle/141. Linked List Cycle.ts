// 141. Linked List Cycle
// Дано: массив целочисленных чисел. Это связанный список. 
// Условие: вернуть true, если связанный список имеет цикл внутри, в обратном случае - false.
// Элементы идут поочередно и нужно понять с каким элементом у него есть связь - цикл. Цикл обозначает то, что мы с последнего элемента возвращаемся на pos элемент и такой цикл бесконечный. 

// const head1 = [3,2,0,-4]
// const head2 = [1,2]
// const head3 = [1]
// const head4 = [9, 10, 8, 12, 4]

class ListNode {
    val: number // Текущий элемент списка
    next: ListNode | null // Указывает на следующий элемент списка
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

const node4 = new ListNode(-4)
const node3 = new ListNode(0, node4)
const node2 = new ListNode(2, node3)
const node1 = new ListNode(3, node2)

node4.next = node2

function hasCycle(head: ListNode | null): boolean {
    if (!head) return false

    let slow = head
    let fast = head

    while (fast && fast.next) {
        slow = slow.next!
        fast = fast.next.next!
        if (slow.val === fast.val) return true
    }

    return false
};


console.log(hasCycle(node1));

export { }