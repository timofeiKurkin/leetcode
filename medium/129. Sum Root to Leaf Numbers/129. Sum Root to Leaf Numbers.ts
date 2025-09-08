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
function sumNumbers(root: TreeNode | null): number {
    const collectPaths = (tree: TreeNode | null, path: string, paths: number[]) => {
        if (!tree)
            return

        path = path + tree.val

        if (!tree.left && !tree.right)
            paths.push(Number(path))
        else {
            collectPaths(tree.left, path, paths)
            collectPaths(tree.right, path, paths)
        }

        path = path.slice(0, path.length - 1)
    }

    const treePaths: number[] = []
    collectPaths(root, "", treePaths)

    let sum = 0
    for (const res of treePaths) {
        sum += res
    }

    return sum
};

export {}