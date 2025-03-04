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


function binaryTreePaths(root: TreeNode | null): string[] {
    if (!root)
        return []

    const run = (tree: TreeNode | null, path: string[], res: string[]) => {
        if (!tree)
            return

        path.push(`${tree.val}`)

        if (!tree.left && !tree.right)
            res.push(path.join("->"))
        else {
            run(tree.left, path, res)
            run(tree.right, path, res)
        }

        path.pop()
    }

    const res: string[] = []
    run(root, [], res)
    return res
};