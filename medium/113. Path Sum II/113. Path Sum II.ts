import { buildTree } from "../../buildTree"

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

function pathSum(root: TreeNode | null, targetSum: number): number[][] {
    const run = (tree: TreeNode | null, target: number, currPath: number[]): number[][] => {
        if (!tree) {
            currPath.pop()
            return []
        }
        if (!tree.right && !tree.left)
            if (target - tree.val == 0)
                return [currPath.concat(tree.val)]
            else
                return []
        currPath.push(tree.val)
        return run(tree.left, target - tree.val, currPath).concat(run(tree.right, target - tree.val, currPath))
    }
    return run(root, targetSum, [])

    // const result: number[][] = []

    // const run = (tree: TreeNode | null, target: number, path: number[]) => {
    //     if (!tree)
    //         return

    //     path.push(tree.val)
    //     if (!tree.left && !tree.right && target === tree.val)
    //         result.push([...path])
    //     run(tree.left, target - tree.val, path)
    //     run(tree.right, target - tree.val, path)
    //     path.pop()
    // }

    // run(root, targetSum, [])
    // return result
};

const values1 = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1];
const values2 = [1, 2, 3];
const values3 = [1, 2];

const tree1 = buildTree(values1);
const tree2 = buildTree(values2);
const tree3 = buildTree(values3);

console.log(pathSum(tree1, 22))
console.log(pathSum(tree2, 5))
console.log(pathSum(tree3, 0))

export { }