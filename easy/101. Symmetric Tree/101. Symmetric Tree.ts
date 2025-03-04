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

function isSymmetric(root: TreeNode | null): boolean {
    // if (!root?.left && !root?.right)
    //     return true
    // if (!root || (!root.left || !root.right))
    //     return false

    // const queue: (TreeNode | null)[] = [root.left, root.right]

    // while (queue.length) {
    //     const level_len = queue.length
    //     const level_items: (number | null)[] = []

    //     for (let i = 0; i < level_len; i++) {
    //         const item = queue.shift()
    //         level_items.push(item ? item.val : null)

    //         if (item) {
    //             queue.push(item.left)
    //             queue.push(item.right)
    //         }
    //     }

    //     if (level_items.length % 2 !== 0)
    //         return false
    //     else {
    //         let f_i = 0, s_i = level_items.length - 1
    //         while (f_i < s_i) {
    //             if (level_items[f_i] !== level_items[s_i])
    //                 return false
    //             f_i += 1
    //             s_i -= 1
    //         }
    //     }
    // }

    // return true

    if (!root)
        return false

    const checkIfNodesAreContrary = (p: TreeNode | null, q: TreeNode | null) => {
        if (!p && !q) {
            return true;
        }

        if (!p || !q) {
            return false;
        }

        if (p.val !== q.val) {
            return false;
        }

        return checkIfNodesAreContrary(p.right, q.left) && checkIfNodesAreContrary(q.right, p.left)
    }

    return checkIfNodesAreContrary(root.left, root.right);
};