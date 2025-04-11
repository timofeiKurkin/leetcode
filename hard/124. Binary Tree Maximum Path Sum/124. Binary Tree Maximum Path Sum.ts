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

function maxPathSum(root: TreeNode | null): number {
    let maxPath = -Infinity

    const dfs = (root: TreeNode | null): number => {
        if (!root)
            return 0

        const leftTree = Math.max(dfs(root.left), 0)
        const rightTree = Math.max(dfs(root.right), 0)

        const currSum = root.val + leftTree + rightTree
        maxPath = Math.max(currSum, maxPath)

        return root.val + Math.max(leftTree, rightTree)
    }

    dfs(root)
    return maxPath
};

export { }

