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

function invertTree(root: TreeNode | null): TreeNode | null {
    if (!root)
        return null

    if (root.left && root.right) {
        root = new TreeNode(root.val, root.right, root.left)
        return root
    }

    root = new TreeNode(root.val, invertTree(root.right), invertTree(root.left))

    return root
};

export { }

