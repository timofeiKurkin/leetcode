/**
 * Definition for _Node.
 */

class _Node {
    val: number
    left: _Node | null
    right: _Node | null
    next: _Node | null

    constructor(val?: number, left?: _Node, right?: _Node, next?: _Node) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
        this.next = (next === undefined ? null : next)
    }
}

function connect(root: _Node | null): _Node | null {
    const queue = [root]

    while (queue.length) {
        const levelSize = queue.length
        let prev: _Node | null = null

        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift()

            if (node) {
                if (prev == null) {
                    prev = node
                } else {
                    prev.next = node
                    prev = node
                }

                if (node.left) queue.push(node.left)
                if (node.right) queue.push(node.right)
            }

        }

        if (prev !== null) {
            prev.next = null
        }
    }

    return root
};


export { }

