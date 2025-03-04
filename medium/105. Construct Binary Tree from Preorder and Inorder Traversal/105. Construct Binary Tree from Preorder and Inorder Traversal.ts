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

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    if (!preorder.length || !inorder.length)
        return null

    const head = preorder.shift()!
    const index = inorder.indexOf(head)

    const left = buildTree(preorder, inorder.slice(0, index))
    const right = buildTree(preorder, inorder.slice(index + 1,))

    return new TreeNode(head, left, right)
};