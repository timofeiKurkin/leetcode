/**
 * Definition for a binary tree node.
 */

class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

function rightSideView(root: TreeNode | null): number[] {
    if (root == null) {
        return []
    }

    const res = []
    const queue = [root]

    while (queue.length) {
        let rightVal = 0
        const levelSize = queue.length

        for (let i = 0; i <= levelSize; i++) {
            const node = queue.shift()!

            if (i == levelSize - 1) {
                rightVal = node.val
            }

            if (node.left) {
                queue.push(node.left)
            }
            if (node.right) {
                queue.push(node.right)
            }
        }

        res.push(rightVal)
    }

    return res
};

export { }
