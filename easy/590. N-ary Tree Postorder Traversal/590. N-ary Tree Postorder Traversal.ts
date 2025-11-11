/**
 * Definition for node.
 * class _Node {
 *     val: number
 *     children: _Node[]
 *     constructor(val?: number) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.children = []
 *     }
 * }
 */

function postorder(root: _Node | null): number[] {
    // return root ? [...root.children.map((ch) => postorder(ch)).flat(), root.val] : []
    const res: number[] = []

    function run(node: _Node | null) {
        if (node) {
            node.children.forEach(run)
            res.push(node.val)
        }
    }

    run(root)
    
    return res
};