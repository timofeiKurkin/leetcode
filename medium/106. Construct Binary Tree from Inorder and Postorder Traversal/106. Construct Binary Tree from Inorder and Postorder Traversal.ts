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

function buildTree(inorder: number[], postorder: number[]): TreeNode | null {
    if (!inorder.length || !postorder.length)
        return null

    const head = postorder.pop()!
    const indexInInorder = inorder.indexOf(head)

    const right_tree = buildTree(inorder.slice(indexInInorder + 1,), postorder)
    const left_tree = buildTree(inorder.slice(0, indexInInorder), postorder)

    return new TreeNode(head, left_tree, right_tree)
};

export { }

