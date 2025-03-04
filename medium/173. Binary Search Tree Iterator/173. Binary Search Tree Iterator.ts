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

class BSTIterator {
    stack: TreeNode[]

    constructor(root: TreeNode | null) {
        this.stack = []
        this.mostLeftInOrder(root)
    }

    mostLeftInOrder(tree: TreeNode | null) {
        if (!tree) return

        while (tree) {
            this.stack.push(tree)
            tree = tree.left
        }
    }

    next(): number {
        const topOfTheStack = this.stack.pop()

        if (!topOfTheStack)
            return -1

        if (topOfTheStack?.right)
            this.mostLeftInOrder(topOfTheStack.right)
        return topOfTheStack.val
    }

    hasNext(): boolean {
        return this.stack.length > 0
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = new BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */