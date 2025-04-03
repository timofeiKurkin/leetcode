/**
 * Definition for _Node.
 */

class _Node {
    val: boolean
    isLeaf: boolean
    topLeft: _Node | null
    topRight: _Node | null
    bottomLeft: _Node | null
    bottomRight: _Node | null
    constructor(val?: boolean, isLeaf?: boolean, topLeft?: _Node, topRight?: _Node, bottomLeft?: _Node, bottomRight?: _Node) {
        this.val = (val === undefined ? false : val)
        this.isLeaf = (isLeaf === undefined ? false : isLeaf)
        this.topLeft = (topLeft === undefined ? null : topLeft)
        this.topRight = (topRight === undefined ? null : topRight)
        this.bottomLeft = (bottomLeft === undefined ? null : bottomLeft)
        this.bottomRight = (bottomRight === undefined ? null : bottomRight)
    }
}


function construct(grid: number[][]): _Node | null {
    const quadTree = (
        x1: number, x2: number,
        y1: number, y2: number
    ): _Node | null => {
        if (x1 === x2 && y1 === y2) {
            return new _Node(!!grid[y1][x1], true)
        }

        const xMiddle = Math.floor((x1 + x2) / 2), yMiddle = Math.floor((y1 + y2) / 2)

        const topLeft = quadTree(x1, xMiddle, y1, yMiddle) || undefined
        const topRight = quadTree(xMiddle + 1, x2, y1, yMiddle) || undefined
        const bottomLeft = quadTree(x1, xMiddle, yMiddle + 1, y2) || undefined
        const bottomRight = quadTree(xMiddle + 1, x2, yMiddle + 1, y2) || undefined

        if (topLeft?.isLeaf && topRight?.isLeaf && bottomLeft?.isLeaf && bottomRight?.isLeaf) {
            if (
                topLeft.val === topRight.val &&
                topRight.val === bottomLeft.val &&
                bottomLeft.val === bottomRight.val
            ) {
                return new _Node(topLeft.val, true)
            }
        }

        return new _Node(true, false, topLeft, topRight, bottomLeft, bottomRight)
    }

    return quadTree(0, grid.length - 1, 0, grid.length - 1)
};