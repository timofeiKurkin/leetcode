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

function kthSmallest(root: TreeNode | null, k: number): number {
    const inOrder = (tree: TreeNode | null): number[] => {
        if (!tree)
            return []

        return [...inOrder(tree.left), tree.val, ...inOrder(tree.right)]
    }

    return inOrder(root)[k - 1]
};

export { }
