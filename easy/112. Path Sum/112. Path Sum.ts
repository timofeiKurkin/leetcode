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

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
    const run = (tree: TreeNode | null, target: number) => {
        if (!tree)
            return false

        if (!tree.right && !tree.left)
            return target - tree.val == 0

        return run(tree.left, target - tree.val) || run(tree.right, target - tree.val)
    }

    return run(root, targetSum)
};

export { }