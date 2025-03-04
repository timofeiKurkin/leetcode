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

function minDepth(root: TreeNode | null): number {
    if (!root) return 0

    const queue = [root]

    let depth = 0

    while (queue.length > 0) {
        const levelSize = queue.length
        depth += 1

        for (let i = 0; i < levelSize; i++) {
            const currentNode = queue.shift()!

            if (!currentNode.left && !currentNode.right) {
                return depth
            } else {
                if (currentNode.left) queue.push(currentNode.left)
                if (currentNode.right) queue.push(currentNode.right)
            }
        }
    }

    return queue.length
};

export { }