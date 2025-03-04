// 234. Palindrome Linked List
// Дано: связанный список. 
// Условие: вернуть true если список является палиндромом, в обратном случае - false. Палиндром - последовательность, которая читается одинаково и вперед, и назад.

// Пример 1
// Input: head = [1,2,2,1]
// Output: true

// Пример 2
// Input: head = [1,2]
// Output: false

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

// const node5 = new ListNode(1)
// const node4 = new ListNode(2, node5)
const node3 = new ListNode(2)
const node2 = new ListNode(2, node3)
const node1 = new ListNode(1, node2)

function isPalindrome(head: ListNode | null): boolean {
    if(head && !head.next) true

    // let newHead: ListNode | null = new ListNode(head?.val)

    // let prev: ListNode | null = new ListNode(head?.val)
    // let copy: ListNode | null = newHead
    // let curr = head?.next

    // while(curr) {
    //     let next = curr.next
    //     curr.next = prev
    //     prev = curr
    //     copy.next = new ListNode(curr.val)
    //     copy = copy?.next
    //     curr = next
    // }

    // while(prev && newHead) {
    //     if (prev.val === newHead.val) {
    //         prev = prev.next
    //         newHead = newHead.next
    //     } else {
    //         return false
    //     }
    // }

    // return true

    let prev: ListNode | null = null
    let fast = head
    let slow: ListNode | null = head

    while(fast && fast.next && slow) {
        fast = fast.next.next

        let next = slow.next
        slow.next = prev
        prev = slow
        slow = next
    }

    if(fast) {
        slow = slow!.next
    }

    while(prev && slow) {
        if (prev.val === slow.val) {
            prev = prev.next
            slow = slow.next
        } else {
            return false
        }
    }

    // [1,1,2,1]
    return true
};

console.log(isPalindrome(node1));


export { }
