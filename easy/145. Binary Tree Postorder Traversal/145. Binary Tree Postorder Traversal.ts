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

function postorderTraversal(root: TreeNode | null): number[] {
    return solution2(root)
};

function solution1(root: TreeNode | null): number[] {
    if (!root) return []
    return [...postorderTraversal(root.left), ...postorderTraversal(root.right), root.val]
}

function solution2(root: TreeNode | null, res: number[] = []): number[] {
    if (!root) return []
    if (root) {
        res.push(root.val)
        solution2(root.left)
        solution2(root.right)
    }

    return res
}

function solution3(root: TreeNode | null): number[] {
    if (!root) return []
    const res: number[] = []
    const stack: TreeNode[] = []
    let current: TreeNode | null = root
    let lastVisited: TreeNode | null = null

    while (stack.length || current) {
        if (current) {
            stack.push(current)
            current = current.left
        } else {
            const node = stack[stack.length - 1]
            if (node.right && node.right !== lastVisited) {
                current = node.right
            } else {
                stack.pop()
                lastVisited = node
                res.push(node.val)
            }
        }
    }

    return res
}

export { }

