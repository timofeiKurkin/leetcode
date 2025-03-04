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

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    // if (!p && !q) return true

    // const pQueue = [p]
    // const qQueue = [q]

    // while (pQueue.length && qQueue.length) {
    //     const levelSizeP = pQueue.length
    //     const levelSizeQ = qQueue.length
    //     if (levelSizeP !== levelSizeQ) return false

    //     for (let i = 0; i < levelSizeP; i++) {
    //         const currentNodeP = pQueue.shift()!
    //         const currentNodeQ = qQueue.shift()!

    //         if (currentNodeP && currentNodeQ) {
    //             if (currentNodeP.val !== currentNodeQ.val) return false

    //             if (currentNodeP.right || currentNodeQ.right) {
    //                 pQueue.push(currentNodeP.right)
    //                 qQueue.push(currentNodeQ.right)
    //             }

    //             if (currentNodeP.left || currentNodeQ.left) {
    //                 pQueue.push(currentNodeP.left)
    //                 qQueue.push(currentNodeQ.left)
    //             }
    //         } else return false
    //     }
    // }

    // return true

    if (!p && !q) return true
    if (!p || !q || p.val !== q.val) return false
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
};

export { }