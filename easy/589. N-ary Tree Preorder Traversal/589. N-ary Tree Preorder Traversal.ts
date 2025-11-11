/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     children: _Node[]
 * 
 *     constructor(val?: number, children?: _Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.children = (children===undefined ? [] : children)
 *     }
 * }
 */


function preorder(root: _Node | null): number[] {
    // return root ? [root.val, ...root.children.map((ch) => preorder(ch)).flat()] : []
    const res: number[] = []

    function run(node: _Node | null) {
        if (node) {
            res.push(node.val)
            node.children.forEach(run)
        }
    }

    run(root)

    return res
};