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

function sortedArrayToBST(nums: number[]): TreeNode | null {
    if (!nums.length)
        return null

    const middle = ~~(nums.length / 2)
    const left = sortedArrayToBST(nums.slice(0, middle))
    const right = sortedArrayToBST(nums.slice(middle + 1,))
    return new TreeNode(nums[middle], left, right)
};