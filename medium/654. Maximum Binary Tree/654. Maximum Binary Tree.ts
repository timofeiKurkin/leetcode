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

function constructMaximumBinaryTree(nums: number[]): TreeNode | null {
    if (!nums.length) {
        return null
    }

    let maxValue = [-1, 0]

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > maxValue[0]) {
            maxValue = [nums[i], i]
        }
    }

    return new TreeNode(
        maxValue[0],
        constructMaximumBinaryTree(nums.slice(0, maxValue[1])),
        constructMaximumBinaryTree(nums.slice(maxValue[1] + 1,))
    )
};

export { }

