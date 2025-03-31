/**
 * Definition for _Node.
 */

class _Node {
    val: number
    next: _Node | null
    random: _Node | null

    constructor(val?: number, next?: _Node, random?: _Node) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
        this.random = (random === undefined ? null : random)
    }
}

function copyRandomList(head: _Node | null): _Node | null {
    if (!head)
        return null

    const nodes = new Map<_Node, _Node>()
    let curr: _Node | null = head
    while (curr) {
        nodes.set(curr, new _Node(curr.val))
        curr = curr.next
    }

    curr = head
    while (curr) {
        nodes.get(curr)!.next = curr.next ? nodes.get(curr.next)! : null
        nodes.get(curr)!.random = curr.random ? nodes.get(curr.random)! : null
        curr = curr.next
    }

    return nodes.get(head) || null
};

export { }

