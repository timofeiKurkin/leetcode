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

function diameterOfBinaryTree(root: TreeNode | null): number {
    let diameter = 0

    const run = (tree: TreeNode | null): number => {
        if (!tree)
            return 0
        if (!tree.left && !tree.right)
            return 1

        const left = run(tree.left)
        const right = run(tree.right)

        const max_depth = Math.max(left, right) + 1
        diameter = Math.max(diameter, left + right)
        return max_depth
    }

    run(root)

    return diameter
};

export {}