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

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    let nodes: ListNode[] = []

    lists.forEach((node) => {
        while (node) {
            nodes.push(node)
            node = node.next
        }
    })

    nodes.sort((node1, node2) => node1.val - node2.val)

    let newList = nodes[0] || null
    nodes.forEach((node, index, arr) => {
        node.next = arr[index + 1] || null
    })

    return newList
};

export { }

