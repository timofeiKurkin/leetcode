

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

function levelOrder(root: TreeNode | null): number[][] {
    if (!root) return []

    const res: number[][] = []
    const queue: TreeNode[] = [root]

    while (queue.length > 0) {
        const levelItems: number[] = []
        const levelSize = queue.length

        for (let i = 0; i < levelSize; i++) {
            const currentNode = queue.shift()!

            levelItems.push(currentNode.val)
            if (currentNode.left) queue.push(currentNode.left)
            if (currentNode.right) queue.push(currentNode.right)
        }

        res.push(levelItems)
    }

    res.reverse()
    return res
};

export { }