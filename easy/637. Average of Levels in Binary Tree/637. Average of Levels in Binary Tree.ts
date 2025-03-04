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

function averageOfLevels(root: TreeNode | null): number[] {
    if (!root) return []
    if (root && !root.left && !root.right) return [root.val]
    // if(root && root.left && !root.left.left && !root.left.right && !root.right) return [root.val, root.left.val]
    // if(root && !root.left && root.right && !root.right.left && !root.right.right) return [root.val, root.right.val]

    // const res = [root.val, (root.left.val + root.right.val) / 2]
    const res: number[] = []
    const queue: TreeNode[] = [root]

    while (queue.length > 0) {
        let levelSum = 0
        const levelSize = queue.length

        for (let i = 0; i <= levelSize; i++) {
            const currentNode = queue.shift()!
            levelSum += currentNode.val

            if (currentNode.left) queue.push(currentNode.left)
            if (currentNode.right) queue.push(currentNode.right)
        }

        res.push(levelSum / levelSize)
    }

    return res

    // let right = root
    // let left = root
    // while (right.right) {
    //     if (right.right && right.left) {
    //         res.push((right.left.val + right.right.val) / 2)
    //     } else {
    //         res.push(right.right.val || right.left.val)
    //     }
    //     right = right.right
    // }
    // while (left.left) {
    //     if (left.left && left.right) {
    //         res.push((left.left.val + left.right.val) / 2)
    //     } else {
    //         res.push(left.left.val || left.right.val)
    //     }
    //     left = left.left
    // }
    // return res
};

export { }