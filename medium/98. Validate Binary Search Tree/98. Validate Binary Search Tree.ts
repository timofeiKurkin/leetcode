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

function isValidBST(root: TreeNode | null): boolean {
    const stack: TreeNode[] = []
    let prev: number | null = null
    let curr = root

    while (stack.length || curr) {
        while (curr) {
            stack.push(curr)
            curr = curr.left
        }

        curr = stack.pop()!

        if (prev !== null && curr.val <= prev) {
            return false
        }

        prev = curr.val
        curr = curr.right
    }

    return true
};

export { }
