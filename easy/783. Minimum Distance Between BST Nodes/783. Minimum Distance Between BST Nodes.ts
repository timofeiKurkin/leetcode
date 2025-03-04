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

function getMinimumDifference(root: TreeNode | null): number {
    function run(tree: TreeNode | null, prev: number | null, minimum: number): [number | null, number] {
        if (!tree)
            return [prev, minimum]

        const [prevLeft, minLeft] = run(tree.left, prev, minimum)

        if (prevLeft !== null)
            minimum = Math.min(minLeft, tree.val - prevLeft)

        const newPrev = tree.val

        return run(tree.right, newPrev, minimum)
    }

    const [_, res] = run(root, null, Infinity)
    return res
};